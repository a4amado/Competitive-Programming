import os
from collections import defaultdict

def count_files_in_directories(root_dir):
    problem_count = defaultdict(int)
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            dirnames.remove('.git')  # Exclude .git directory
        dir_name = os.path.basename(dirpath)
        if dir_name != os.path.basename(root_dir):
            problem_count[dir_name] += len(filenames)
        for filename in filenames:
            file_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
            all_files.append(file_path)
    return problem_count, all_files

def generate_markdown(problem_count, all_files):
    total_problems = sum(problem_count.values())
    md_content = f"# Coding Problems Summary\n\n"
    md_content += f"Total problems solved: {total_problems}\n\n"
    md_content += "## Problems by Platform\n\n"
    for platform, count in sorted(problem_count.items()):
        md_content += f"- {platform}: {count}\n"
    md_content += "\n## All Files\n\n"
    for file in sorted(all_files):
        md_content += f"- {file}\n"
    return md_content

def main():
    root_dir = '.'  # Current directory
    problem_count, all_files = count_files_in_directories(root_dir)
    md_content = generate_markdown(problem_count, all_files)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("Summary generated in 'README.md'")

if __name__ == "__main__":
    main()