# https://github.com/YewYew/The-Matchless-Kungfu-Meridians-Tool/

# This script calculates the most skills you can activate in a singular meridian path.
# Do note that this is not necessarily the best way to set up your meridians, because you can:
# a.) Have multiple meridian paths.
# b.) Have meridian paths end at other meridian path points instead of the center. (aka "Doubling-Up")
#     - This gives you the meridian bonus twice.
#     - Can be more space efficient.

# All your internal skills should be put in the list below, free ones like "Primordial Chaos" are unnecessary.
# The repository comes loaded with some placeholders, I recommend replacing them with your actual skills.
# The first part is the skill name, the second is the pattern. The pattern goes as such:
# O is a circle meridian.
# T is a triangle meridian.
# S is a square meridian.
# You can make the pattern symbols whatever you want as long as you're consistent.

skills = {
    "Demo Slayer Arhat": "TTSSOO",
    "Heart-burning Spell": "SST",
}

#This is how many Meridians you have, determines maximum length of a pattern combo.
meridians_count = 8

###########################
#### CODE BEGINS HERE. ####
###########################

# This needs more comments... whatever...

# Esoteric code which concatinates and/or overlaps the patterns.
def concatenate_with_overlap(str1, str2):
	max_overlap = min(len(str1), len(str2))
	for i in range(max_overlap, 0, -1):
		if str1[-i:] == str2[:i]:
			return str1 + str2[i:]
	return str1 + str2

def find_maximum_concatenation(skills, meridians_count):
	skill_patterns = list(skills.values())
	skill_names = list(skills.keys())
	n = len(skill_patterns)

	# Initialize DP (Dynamic Programming) arrays for the calculation(s) size/skill list/pattern.
	dp_skills_count = [0] * (1 << n)
	dp_used_skills = [[] for _ in range(1 << n)]
	dp_patterns = [''] * (1 << n)
	pattern_set = set()  # Set (Unordered List) used for the patterns.

	# Calculate all valid concatenated patterns.
	for i in range(1 << n):
		current_pattern = ''
		current_skills = []
		for j in range(n):
			if i & (1 << j):
				new_pattern = concatenate_with_overlap(current_pattern, skill_patterns[j])
				if len(new_pattern) <= meridians_count:
					current_pattern = new_pattern
					current_skills.append(skill_names[j])
					dp_skills_count[i] = len(set(current_skills))  # Count unique skills.
					dp_used_skills[i] = current_skills # Add the skills to the "blacklist".
					dp_patterns[i] = current_pattern # Add the pattern itself.

	# Store unique patterns in the set.
	if current_pattern not in pattern_set:
		pattern_set.add(current_pattern)

	# Find the maximum number of unique skills used in the patterns.
	max_skills_count = max(dp_skills_count)

	# Collect patterns with the maximum number of unique skills (Best).
	best_patterns = []
	seen_patterns = set()  # For tracking seen patterns to prevent duplicates.

	for i in range(1 << n):
		if dp_skills_count[i] == max_skills_count:
			if dp_patterns[i] not in seen_patterns:  # Check if pattern is unique.
				best_patterns.append((len(dp_patterns[i]), dp_used_skills[i], dp_patterns[i]))
				seen_patterns.add(dp_patterns[i])  # Mark pattern as duplicate (Seen).

	return best_patterns

def __main__():
	best_patterns = find_maximum_concatenation(skills, meridians_count)

	# Print all best patterns found.
	print(f"{len(best_patterns)} combinations found.")
	print("==============================")
	print("------------------------------")
	for pattern_length, best_skills, best_pattern in best_patterns:
		print(f"Pattern Length: {pattern_length} / {meridians_count}")
		print(f"Skills ({len(best_skills)}):")
		for sk in best_skills:
			print("  " + sk)
		print(f"{best_pattern}")
		print("------------------------------")
	input("\nPress any key to exit.")
	
if __name__ == "__main__":
	__main__()

# https://github.com/YewYew/The-Matchless-Kungfu-Meridians-Tool/