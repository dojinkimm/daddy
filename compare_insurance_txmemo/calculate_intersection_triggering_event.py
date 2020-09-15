import csv


bs2_t0 = set()
with open('bs2.csv', newline='') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        bs2_t0.add(i.get('json.event.subject_id: Descending'))

insurance_t0 = set()
with open('insurance.csv', newline='') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        insurance_t0.add(i.get('json.event.subject_id: Descending'))

bs2_c = set()
with open('bs2_control.csv', newline='') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        bs2_c.add(i.get('json.event.subject_id: Descending'))


insurance_c = set()
with open('insurance_control.csv', newline='') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        insurance_c.add(i.get('json.event.subject_id: Descending'))


bs2_c_insurance_c = bs2_c.intersection(insurance_c)
bs2_t0_insurance_t0 = bs2_t0.intersection(insurance_t0)
bs2_t0_insurance_c = bs2_t0.intersection(insurance_c)
bs2_c_insurance_t0 = bs2_c.intersection(insurance_t0)

print(len(bs2_c_insurance_c))
print(len(bs2_t0_insurance_t0))
print(len(bs2_t0_insurance_c))
print(len(bs2_c_insurance_t0))

# 4137 bs2 control && insurance control
# 4135 bs2 t0 && insurance t0
# 4157 bs2 t0 && insurance control
# 4119 bs2 control && insurance t0

# 8292 - bs2
# 8256 - bs2 control
# 8255 - insurance
# 8294 - insurance control

intersected = 4137+4135+4157+4119
total = 8292+8256+8255+8294
print(intersected)
print(intersected*2)
print(total)
