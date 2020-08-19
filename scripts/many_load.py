import csv  # https://docs.python.org/3/library/csv.html

from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        c , created = Category.objects.get_or_create(name=row[7])
        s , created = States.objects.get_or_create(name=row[8])
        r , created = Region.objects.get_or_create(name=row[9])
        i , created = Iso.objects.get_or_create(name=row[10])

        try:
            y=int(row[3])
        except:
            y=None

        try:
            z=float(row[4])
        except:
            z=None

        try:
            x=float(row[5])
        except:
            x=None

        if row[6]=="":
            w=None
        else:
            w=float(row[6])

        try:
            j=row[2]
        except:
            j=None

        site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x, area_hectares= w, category=c, states=s, region=r, iso=i)
        site.save()