package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/empirelabs/aip"
)

func main() {
	stat, err := os.Stdin.Stat()
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: cannot stat stdin: %v\n", err)
		os.Exit(1)
	}

	if (stat.Mode() & os.ModeCharDevice) != 0 {
		fmt.Fprintln(os.Stderr, "usage: cat receipt.json | aip")
		fmt.Fprintln(os.Stderr, "  Reads a JSON Receipt from stdin and validates it.")
		os.Exit(1)
	}

	data, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: cannot read stdin: %v\n", err)
		os.Exit(1)
	}

	if len(data) == 0 {
		fmt.Fprintln(os.Stderr, "error: empty input")
		os.Exit(1)
	}

	var receipt aip.Receipt
	if err := json.Unmarshal(data, &receipt); err != nil {
		fmt.Fprintf(os.Stderr, "validation failed: invalid JSON: %v\n", err)
		os.Exit(1)
	}

	if receipt.ID == "" {
		fmt.Fprintln(os.Stderr, "validation failed: missing required field 'id'")
		os.Exit(1)
	}
	if receipt.Protocol == "" {
		fmt.Fprintln(os.Stderr, "validation failed: missing required field 'protocol'")
		os.Exit(1)
	}
	if receipt.Version == "" {
		fmt.Fprintln(os.Stderr, "validation failed: missing required field 'version'")
		os.Exit(1)
	}
	if receipt.Timestamp.IsZero() {
		fmt.Fprintln(os.Stderr, "validation failed: missing required field 'timestamp'")
		os.Exit(1)
	}

	out, _ := json.MarshalIndent(receipt, "", "  ")
	fmt.Println("✓ Receipt valid:")
	os.Stdout.Write(out)
	fmt.Println()
}
