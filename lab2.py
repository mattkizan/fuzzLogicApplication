
import matplotlib.pyplot as plt
def visualize_fuzzy_sets_output(r1,r2,r3,r4):
    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('steering')
    x = [ 0, 0, 60]
    y = [ 1, 1, 0]
    x2 = [ 40, 100, 100]
    y2 = [ 0, 1, 1,]
    x3 = [ 30, 50, 70]
    y3 = [ 0, 1, 0]
    plt.plot(x,y, 'r-', label='hard left')
    plt.plot(x2,y2, 'b-', label='hard right')
    plt.plot(x3, y3, 'g-', label='straight')
    plt.xlim(0, 100)
    plt.ylim(0, 1.1)
    plt.axhline(y=r1, color='c', linestyle='-', label='rule1')
    plt.axhline(y=r2, color='m', linestyle='-',label='rule2')
    plt.axhline(y=r3, color='y', linestyle='-', label='rule3')
    plt.axhline(y=r4, color='k', linestyle='-', label='rule4')
    plt.legend()
    plt.show()
    plt.figure()

def visualize_fuzzy_sets_input(ls,rs):

    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('LS')
    x = [ 0, 0, 30]
    y = [ 1, 1, 0]
    x2 = [ 20, 50, 50]
    y2 = [ 0, 1, 1,]
    plt.plot(x,y, 'r-', label='obstacle near')
    plt.plot(x2,y2, 'b-', label='obstacle far')
    plt.xlim(0, 50)
    plt.ylim(0, 1.1)
    # only one line may be specified; full height
    plt.axvline(x=ls, color='purple', label='axvline - full height')

    plt.legend()
    plt.show()
    plt.figure()


    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('RS')
    x = [ 0, 0, 30]
    y = [ 1, 1, 0]
    x2 = [ 20, 50, 50]
    y2 = [ 0, 1, 1,]
    plt.plot(x,y, 'r-', label='obstacle near')
    plt.plot(x2,y2, 'b-', label='obstacle far')
    plt.xlim(0, 50)
    plt.ylim(0, 1.1)
    plt.axvline(x=rs, color='purple', label='axvline - full height')
    plt.legend()
    plt.show()
    plt.figure()


def visualize_fuzzy_sets():
    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('LS')
    x = [ 0, 0, 30]
    y = [ 1, 1, 0]
    x2 = [ 20, 50, 50]
    y2 = [ 0, 1, 1,]
    plt.plot(x,y, 'r-', label='obstacle near')
    plt.plot(x2,y2, 'b-', label='obstacle far')
    plt.xlim(0, 50)
    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()
    plt.figure()


    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('RS')
    x = [ 0, 0, 30]
    y = [ 1, 1, 0]
    x2 = [ 20, 50, 50]
    y2 = [ 0, 1, 1,]
    plt.plot(x,y, 'r-', label='obstacle near')
    plt.plot(x2,y2, 'b-', label='obstacle far')
    plt.xlim(0, 50)
    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()
    plt.figure()


    plt.xlabel(' Distance cm')
    plt.ylabel('degree of membership')
    plt.title('steering')
    x = [ 0, 0, 60]
    y = [ 1, 1, 0]
    x2 = [ 40, 100, 100]
    y2 = [ 0, 1, 1,]
    x3 = [ 30, 50, 70]
    y3 = [ 0, 1, 0]
    plt.plot(x,y, 'r-', label='hard left')
    plt.plot(x2,y2, 'b-', label='hard right')
    plt.plot(x3, y3, 'g-', label='straight')
    plt.xlim(0, 100)
    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()
    plt.figure()




def fuzzificationNear(x, a, b, c):
    if x < a or x > c:
        return 0
    if b <= x < c:
        return (c - x) / (c - b)

    else:
        return 0

def fuzzificationfar(x, a, b, c):
    if x < a or x > c:
        return 0
    if a <= x < b:
        return (x - a) / (b - a)
    else:
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    visualize_fuzzy_sets()
    ls = float(input("Enter the left sonar sensor reading (0-50): "))
    rs = float(input("Enter the right sonar sensor reading (0-50): "))

    visualize_fuzzy_sets_input(ls,rs)

    LsNearMembership = fuzzificationNear(ls,0,0,30)
    LsfarMembership = fuzzificationfar(ls,20,50,50)
    RsNearMembership = fuzzificationNear(rs,0,0,30)
    RsfarMembership = fuzzificationfar(rs,20,50,50)



    # IF LS is "Near" AND RS is "Near" THEN Steering Angle is "Hard Right"
    rule1 = min(LsNearMembership, RsNearMembership)
    # IF LS is "Near" AND RS is "Far" THEN Steering Angle is "Hard Right"
    rule2 = min(LsNearMembership, RsfarMembership)
    # IF LS= is "Far" AND RS is "Near" THEN Steering Angle is "Hard left"
    rule3 = min(LsfarMembership, RsNearMembership)
    # IF LS is "Far" AND RS is "Far" THEN Steering Angle is "Straight"
    rule4 = min(LsfarMembership, RsfarMembership)

    print("rule1 hard right:    " + str(rule1))
    print("rule2 hard right:    " + str(rule2))
    print("rule3 hard left:    " + str(rule3))
    print("rule4 straight:    " + str(rule4))



    visualize_fuzzy_sets_output(rule1, rule2,rule3, rule4)

# using python library