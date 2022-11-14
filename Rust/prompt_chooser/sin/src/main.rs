use value_chooser::get_output;
use clap::Parser;

/// Adds the appropriate tokens of the CLI to the PS1 Global Variable
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// The command to print out the appropriate token
    command: String,

    /// The reference file to print names from
    ref_file: String
}

fn main() {
    let args = Args::parse();
    println!("{}", get_output(&args.command, &args.ref_file));
}
