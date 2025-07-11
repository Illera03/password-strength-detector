output_path = "data/rock_you_filtered.txt"
input_path = "data/rockyou.txt"

with open(input_path, "r", encoding="latin1") as f:
    lines = set(line.strip() for line in f if 8 <= len(line.strip()) <= 16) # Filter passwords by length
    
# Only keep the first 1000000 passwords
#lines = list(lines)[:1000000]

with open(output_path, "w", encoding="utf-8") as out:
    for line in lines:
        out.write(line + "\n")

print(f"{len(lines)} filtered passwords saved to {output_path}")