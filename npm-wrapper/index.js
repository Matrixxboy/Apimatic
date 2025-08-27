#!/usr/bin/env node

const { spawn } = require("child_process");
const args = process.argv.slice(2);

const proc = spawn(process.env.PYTHON || (process.platform === "win32" ? "python" : "python3"), 
  ["-m", "Apimatic.cli", ...args], 
  { stdio: "inherit" }
);

proc.on("close", code => process.exit(code));
