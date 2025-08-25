const { spawn } = require("child_process");
const args = process.argv.slice(2);
const proc = spawn(process.env.PYTHON || "python3", ["-m",
"Apimatic", ...args], {
stdio: "inherit",
});
proc.on("close", code => process.exit(code));