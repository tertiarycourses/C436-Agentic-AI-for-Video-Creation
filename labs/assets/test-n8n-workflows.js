const fs = require("fs");
const path = require("path");

const base = __dirname;
const read = (name) => fs.readFileSync(path.join(base, name), "utf8");
const workflow = (name) => JSON.parse(read(name));
const nodeCode = (wf, name) => wf.nodes.find((n) => n.name === name).parameters.jsCode;
const execute = (code, input = {}) =>
  new Function("$input", code)({ first: () => ({ json: input }) });
const replaceLiteral = (code, marker, value) => code.replace(marker, value.replace(/`/g, "\\`"));
const assert = (condition, message) => {
  if (!condition) throw new Error(message);
};

function testPlanning() {
  const wf = workflow("video-planning-agent-workflow.json");
  let load = nodeCode(wf, "Load Exact Production Contract");
  load = replaceLiteral(load, "PASTE_THE_EXACT_LAB_1_PRODUCTION_CONTRACT_JSON_HERE", read("production-contract-approved.json"));
  const contract = execute(load)[0].json;
  const validate = nodeCode(wf, "Validate Contract and Version");
  const plan = nodeCode(wf, "Plan or Block");
  const ready = execute(plan, execute(validate, contract)[0].json)[0].json;
  assert(ready.status === "plan_ready" && ready.publish_allowed === false, "Planning ready path failed.");
  assert(ready.source_fingerprint === "fnv31-91159a8b", "Planning fingerprint differs from the approved storyboard lineage.");
  const blockedInput = { ...contract, approved_facts: [] };
  const blocked = execute(plan, execute(validate, blockedInput)[0].json)[0].json;
  assert(blocked.status === "blocked" && blocked.blockers.includes("missing_approved_facts"), "Planning blocked path failed.");
}

function testAssets() {
  const wf = workflow("asset-request-agent-workflow.json");
  let load = nodeCode(wf, "Load Exact Approved Storyboard");
  load = replaceLiteral(load, "PASTE_THE_EXACT_LAB_3_SCRIPT_STORYBOARD_JSON_HERE", read("script-storyboard-approved.json"));
  const input = execute(load)[0].json;
  const output = execute(nodeCode(wf, "Validate and Build Asset Requests"), input)[0].json;
  assert(output.status === "asset_pack_ready" && output.asset_requests.length === 5, "Asset request path failed.");
  assert(output.plan_source_fingerprint === input.storyboard.plan_source_fingerprint, "Asset request path dropped the Lab 2 plan fingerprint.");
  assert(output.external_action_count === 0, "Asset request workflow executed externally.");
  const noPlanFingerprint = JSON.parse(JSON.stringify(input));
  delete noPlanFingerprint.storyboard.plan_source_fingerprint;
  const blocked = execute(nodeCode(wf, "Validate and Build Asset Requests"), noPlanFingerprint)[0].json;
  assert(blocked.status === "blocked" && blocked.blockers.includes("missing_plan_source_fingerprint"), "Asset request path accepted a storyboard without Lab 2 lineage.");
}

function testReview() {
  const wf = workflow("video-review-agent-workflow.json");
  let load = nodeCode(wf, "Load Exact Review Evidence");
  load = replaceLiteral(load, "PASTE_THE_EXACT_LAB_5_FFPROBE_JSON_HERE", read("rejoin/lab-05/ffprobe-v1.json"));
  load = replaceLiteral(load, "PASTE_THE_EXACT_LAB_3_CAPTIONS_VTT_HERE", read("rejoin/lab-05/captions-v1.vtt"));
  load = replaceLiteral(load, "PASTE_THE_EXACT_LAB_4_ASSET_MANIFEST_CSV_HERE", read("asset-manifest-approved.csv"));
  const evidence = execute(load)[0].json;
  const evaluate = nodeCode(wf, "Evaluate Technical Caption and Rights Evidence");
  const clear = execute(evaluate, evidence)[0].json;
  assert(clear.review_status === "review_clear" && clear.release_allowed === false, "Review clear path failed.");
  const bad = { ...evidence, manifestCsvText: evidence.manifestCsvText.replace("approved_for_course_use", "review_required") };
  const blocked = execute(evaluate, bad)[0].json;
  assert(blocked.review_status === "blocked" && blocked.findings.some((x) => x.issue_id === "RV-RIGHTS"), "Review blocked path failed.");
  const longProbe = JSON.parse(JSON.stringify(evidence.probe));
  longProbe.format.duration = "45.000000";
  const longResult = execute(evaluate, { ...evidence, probe: longProbe })[0].json;
  assert(longResult.findings.some((x) => x.issue_id === "RV-DURATION"), "45-second probe did not block.");
  const invalidVtt = evidence.captionsText.replace("00:00:04.000 --> 00:00:11.000", "00:00:04.000 --> 00:00:03.000");
  const captionResult = execute(evaluate, { ...evidence, captionsText: invalidVtt })[0].json;
  assert(captionResult.findings.some((x) => x.issue_id === "RV-CAPTION"), "Invalid VTT timeline did not block.");
}

function testRelease() {
  const wf = workflow("release-orchestrator-workflow.json");
  const evaluate = nodeCode(wf, "Validate Hash Approval and Build Previews");
  const videoHash = "b".repeat(64);
  const approvalHash = "c".repeat(64);
  const packageManifest = {
    run_id: "HB-001",
    package_version: "release-v1",
    platform: "training_dry_run",
    title: "Three coffee variables",
    description: "Synthetic training package",
    privacy_status: "private",
    contains_synthetic_media: true,
    package_owner: "course learner",
    video: { path: "03-edit/output/vertical-draft-v1.mp4", sha256: videoHash, size_bytes: 463191 },
    captions: { path: "02-create/captions-script-v1.vtt", sha256: "d".repeat(64), size_bytes: 558 },
    rights_manifest: { path: "02-create/asset-manifest.csv", sha256: "e".repeat(64), size_bytes: 1178 },
    final_review_approval: {
      path: "03-edit/final-review-approval.json",
      sha256: approvalHash,
      approval_version: "final-review-v1",
      decision: "APPROVED_FOR_PRIVATE_RELEASE_PACKAGE",
      scope: "private release package only; no public posting",
      reviewed_video_sha256: videoHash
    },
    platform_previews: {
      youtube: { method: "videos.insert", privacyStatus: "private", containsSyntheticMedia: true, execute: false },
      tiktok: { method: "POST /v2/post/publish/video/init/", privacy_level: "SELF_ONLY", is_aigc: true, source: "FILE_UPLOAD", video_size: 463191, chunk_size: 463191, total_chunk_count: 1, execute: false }
    }
  };
  const baseMeta = {
    run_id: "HB-001",
    package_version: "release-v1",
    platform: "training_dry_run",
    title: "Three coffee variables",
    description: "Synthetic training package",
    privacy_status: "private",
    contains_synthetic_media: true,
    caption_path: "02-create/captions-script-v1.vtt",
    video_path: "03-edit/output/vertical-draft-v1.mp4",
    rights_evidence_path: "02-create/asset-manifest.csv",
    package_owner: "course learner",
    package_manifest_path: "04-release/release-package-manifest.json",
    package_manifest: packageManifest,
    package_sha256: "a".repeat(64),
    final_review_approval_path: "03-edit/final-review-approval.json",
    final_review_approval_sha256: approvalHash,
    public_release_allowed: false
  };
  const denied = execute(evaluate, { ...baseMeta, human_decision: "deny" })[0].json;
  assert(denied.status === "denied" && denied.external_action_count === 0, "Release denial failed.");
  const approved = execute(evaluate, {
    ...baseMeta,
    human_decision: "approve_private_dry_run",
    approval_scope: "one private non-executing preview",
    approval_package_sha256: baseMeta.package_sha256,
    approval_expires_at: new Date(Date.now() + 3600000).toISOString()
  })[0].json;
  assert(approved.status === "dry_run_ready" && approved.publish_allowed === false, "Release approval failed.");
  assert(!approved.platform_previews.youtube.execute && !approved.platform_previews.tiktok.execute, "Platform preview executed.");
  const expired = execute(evaluate, { ...baseMeta, human_decision: "approve_private_dry_run", approval_scope: "one preview", approval_package_sha256: baseMeta.package_sha256, approval_expires_at: "2000-01-01T00:00:00Z" })[0].json;
  assert(expired.status === "blocked" && expired.blockers.includes("approval_hash_or_expiry_invalid"), "Expired approval did not block.");
  const changedMetadata = execute(evaluate, { ...baseMeta, title: "Changed after approval", human_decision: "approve_private_dry_run", approval_scope: "one preview", approval_package_sha256: baseMeta.package_sha256, approval_expires_at: new Date(Date.now() + 3600000).toISOString() })[0].json;
  assert(changedMetadata.status === "blocked" && changedMetadata.blockers.includes("package_manifest_mismatch"), "Changed package metadata did not block.");
}

function testAnalytics() {
  const wf = workflow("analytics-scale-workflow.json");
  let load = nodeCode(wf, "Load Exact Analytics Operations and Contract");
  load = replaceLiteral(load, "PASTE_THE_EXACT_SYNTHETIC_VIDEO_ANALYTICS_CSV_HERE", read("synthetic-video-analytics.csv"));
  load = replaceLiteral(load, "PASTE_THE_EXACT_SYNTHETIC_PIPELINE_OPERATIONS_CSV_HERE", read("synthetic-pipeline-operations.csv"));
  load = replaceLiteral(load, "PASTE_THE_EXACT_METRIC_CONTRACT_JSON_HERE", read("metric-contract-approved.json"));
  const input = execute(load)[0].json;
  const output = execute(nodeCode(wf, "Calculate Metrics and Fail Closed"), input)[0].json;
  assert(output.status === "analysis_ready" && output.operations.cost_per_accepted_video_sgd > 0, "Analytics calculation failed.");
  assert(output.recommended_scale_decision === "HOLD", "Operational blocker did not force HOLD.");
  const question = output.summary_by_hook.find((x) => x.hook_family === "question");
  assert(question.video_count === 2 && question.total_views === 7000, "Low-volume row was included in grouped analytics.");
  const cleanOperations = input.operations.map((row) => ({
    ...row,
    unresolved_rights_items: "0",
    blocking_review_findings: "0",
    duplicate_release_actions: "0",
    rollback_tested: "true",
    human_review_capacity_slots: "3",
    human_reviews_required: "1"
  }));
  const rollbackFailure = cleanOperations.map((row, index) => ({
    ...row,
    rollback_tested: index === 0 ? "false" : "true"
  }));
  const rollbackOutput = execute(nodeCode(wf, "Calculate Metrics and Fail Closed"), {
    ...input,
    operations: rollbackFailure
  })[0].json;
  assert(rollbackOutput.recommended_scale_decision === "HOLD" && rollbackOutput.operations.rollback_all_tested === false, "Rollback-only failure did not force HOLD.");
  const duplicateFailure = cleanOperations.map((row, index) => ({
    ...row,
    duplicate_release_actions: index === 0 ? "1" : "0"
  }));
  const duplicateOutput = execute(nodeCode(wf, "Calculate Metrics and Fail Closed"), {
    ...input,
    operations: duplicateFailure
  })[0].json;
  assert(duplicateOutput.recommended_scale_decision === "HOLD" && duplicateOutput.operations.duplicate_release_actions === 1, "Duplicate-release-only failure did not force HOLD.");
}

testPlanning();
testAssets();
testReview();
testRelease();
testAnalytics();
console.log("All five n8n workflow templates PASS ready, blocked, and zero-action checks.");
