def damage(amount,user_input=0,target = 0):
    if target == 0:
        target_class = e_act_cards
    else:
        target_class = f_act_cards
    #user_input is the index of the card in the enemy's active card list
    #amount is the amount of damage to be dealt
    (target_class.card_list[user_input]).defx -= amount
    #maybe should run the remove_card function to get rid of damaged cards if they are killed
    target_class.remove_card()

#HOLDS ALL CARDS AVAILABLE TO BE CURRENTLY ACTIVE
class active_cards():
    def __init__(self):
        self.card_list = [None,None,None,None,None]

    def add(self,card_class):
        #card_class is the class of the new card to be added
        count = 0
        for i in range(len(self.card_list)):
            card = self.card_list[i]
            if card != None:
                if i == 4:
                    print("Active Cards Full")
            else:
                self.card_list[i] = card_class
                break

    def remove_card(self):
        del_count = 0
        for i in range(len(self.card_list)):
            #print(self.card_list)
            card = self.card_list[i]
            if card == None:
                continue
            else:
                if card.defx < 1:
                    self.card_list.pop(i)
                    self.card_list.append(None)
                    self.remove_card()
                    #MUST REDO THIS FUNCTION IN CASE OF SECOND CARD
                    #WILL LIKELY NOT HAPPEN IN REAL SITUATION

#HOLDS DATA PERTAINING TO A **SINGLE** CARD    
class card():
    
    def __init__(self,index):
        self.ability_unavailable = False
        excel_index = index
        self.atx = 10
        self.defx = 0
        
        #somehow read the csv file and get the stuff
        #self.atkx
        #self.defx
        #self.ability_index
            #self.ability_effect_count  #how much damage/stuff
            #self.ability_affect_count  #may be 1 or more cards
        #self.evo_index

    #set ability unavailable after causing damage or smthing
    '''
    def ability(self,self.ability_unavailable=False):
        if self.ability_index == "damage":
            self.ability = damage(self.ability_effect_count)
            self.ability_unavailable = True
        elif self.ability_index == "summon":
            self.ability_unavailable = True
        elif self.ability_index == "add_stats":

        elif self.ability_index == "banish":
            self.ability_unavailable = True
            
    def is_dead(self):
        if self.defx < 1:
            #somehow delete card
    '''

#TESTING
ex_card = card(2)
ex_active = active_cards()
#END TESTING

#REAL USE CASE
f_act_cards = active_cards()
e_act_cards = active_cards()

f_act_cards.add(ex_card)
e_act_cards.add(ex_card)
#END REAL USE CASE
