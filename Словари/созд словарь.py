persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
# data = {}
# for j in range(len(persons)):     #мое решение
#     data.setdefault(persons[j][0],dict(salary= persons[j][1],gender=persons[j][2],passport=persons[j][3]))
data = {}
for info in persons:
    data[info[0]] = {'salary': info[1], 'gender': info[2], 'passport': info[3]}   #скопировал чужое

print(data)
