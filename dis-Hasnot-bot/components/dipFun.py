
import random
# Full list
dipMemberList = ["Hasnat", "Murad", "Ajoy", "Sushanto", "Junayed", "Aong"]


class dipRandom:
    def who():
        result = random.choice(dipMemberList)
        return result
        

    def whoGroup(value):
        result = random.sample(dipMemberList, value)
        return result   

    def givenWhoGroup(value, count):
        try:
            if len(value) == 0:
                return "Must Input List"

            else:
                result = random.sample(value, count)
                return result

        except Exception as e:
            print(e)
            return     
