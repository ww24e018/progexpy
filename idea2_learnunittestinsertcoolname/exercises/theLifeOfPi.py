
def theLifeOfPi_tupel():
    mypi = 3.14159265359
    return (
        "%f!" % mypi,
        "%12f!" % mypi,
        "%12.2f!" % mypi,
        "%10.0f!" % mypi,
        "%13.11f!" % mypi,
        "%015f!" % mypi,
        "%+015.2f!" % mypi,
    )

if __name__ == "__main__":
    for i in theLifeOfPi_tupel():
        print("Pi = %s" % i)