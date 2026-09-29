def format_greeting(name: str, title: str = "Customer") -> str:
	# strip() removes leading and trailing whitespace from the name.
	clean_name = name.strip()

	if not clean_name:
		return "Hello, Valued Customer!"

	# title() capitalizes the first letter of each word.
	titled_name = clean_name.title()
	# split() separates the name into words so the first name can be selected.
	first_name = titled_name.split()[0]

	return f"Hello, {first_name} ({title})!"


if __name__ == "__main__":
	full_name = input("What's your full name? ")
	print(format_greeting(full_name))