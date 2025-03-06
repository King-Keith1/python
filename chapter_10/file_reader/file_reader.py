from pathlib import Path

path = Path('my_name.txt')
contents = path.read_text()
print(contents)

# lines = contents.splitlines()
# for line in lines:
#      print(line)

new_path = Path("new_file.txt")
new_path = "Today was a day that was being a day.\n"
new_path += "Is what David said to us.\n"
new_path += "Not really sure, what he meant by that. We all took it with a grain of salt.\n"
new_path += "By we, I meant my classmates and me, 1.Aidan,\n 2.Asanda,\n 3.Cadee,\n 4.Courtney,\n 5.Ethan,\n 6.Lindo,\n 7.Marvelous,\n 8.Mieke,\n 9.Tom,\n 10.Sibu,\n 11.Ronny.\n"
new_path += "I excluded myself coz I'm the only one who got it.\n"
path.write_text(new_path)