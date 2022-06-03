import math
def optimal_change(item_cost, amount_paid):
    #Build a directory with money*100 to avoid float numbers
    dollars={
        '$100 bill':10000,
        '$50 bill':5000,
        '$20 bill':2000,
        '$10 bill':1000,
        '$5 bill':500,
        '$1 bill':100,
        'quarter':25,
        'dime':10,
        'nickle':5,
        'pennie':1,
    }
    #Don't want any floating numbers 
    paid=math.floor(amount_paid*100)
    cost=math.floor(item_cost*100)
    change=paid - cost
    answer=f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    #if change is only one pennie, get rid of the 'and' in your statement
    if change==1:
        answer+='1 pennie.'
    else:
    #iterate through the values of the directory subtracting the corresponding value from change and adding the correct keys to our answer
        for value in dollars:
            counter=0
            while change>=dollars[value]:
                change-=dollars[value]
                counter+=1
            #before adding it to answer determine whether theres 1 or more times this value is being pushed so you could add the 's' and if it's pennies so you could switch the '.' for a ','
            if counter>1:
                if value=='pennie':
                    answer+=f"and {counter} {value}s."
                else:
                    answer+=f"{counter} {value}s, "
            elif counter== 1:
                if value=='pennie':
                    answer+=f"and 1 {value}."
                else:
                    answer+=f"1 {value}, "
    return answer
    
