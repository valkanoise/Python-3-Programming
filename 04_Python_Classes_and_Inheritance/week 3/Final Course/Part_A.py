
import random


##-------------------##
##      Part A
##-------------------##


class WOFPlayer:
    def __init__(self, name_player):
        self.name = name_player
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney +=  amt
        
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)

##-------------------##
##      Part B
##-------------------##
    

class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrase, guessed):
        player_input = input(('''{} has ${}\n\nCategory: {}\nPhrase:{}\nGuessed: {}\n \nGuess a letter, phrase, or type 'exit' or 'pass': ''').format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
                                
        return '{}'.format(player_input)
    

##-------------------##
##      Part C
##-------------------##

class WOFComputerPlayer(WOFPlayer):
    
# variable del jugador Computer
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name_player, difficulty):
        WOFPlayer.__init__(self, name_player)
        self.difficulty = difficulty

# metodo para definir al azar si el jugador Computer toma una buena o mala decisión    
    def smartCoinFlip(self):
        if random.randint(1,10) > self.difficulty:
            return True
        else:
            return False

# metodo para devolver las letras que aún no han sido adivinadas
    def getPossibleLetters(self, guessed):
        
        not_guessed = []
        
        if self.prizeMoney >= VOWEL_COST: # si jugador tiene > 250 prize que el VOWEL_COST puede adivinar cualquier letra, incluidas las vocales
            not_guessed = [letter for letter in LETTERS if letter not in guessed]
           
            # for letter in LETTERS:
            #     if letter not in guessed:
            #         not_guessed.append(letter)
        
        elif self.prizeMoney < VOWEL_COST: # si el jugador tiene < 250 prize no puede elegir vocales
            not_guessed = [letter for letter in LETTERS if letter not in guessed and letter not in VOWELS]
    
            # for letter in LETTERS:
            #     if letter not in guessed and letter not in VOWELS:
            #         not_guessed.append(letter) 
            
        return not_guessed
                
    
    
    def getMove(self, category, obscuredPhrase, guessed):
        letras_posibles = self.getPossibleLetters(guessed)
        
        if letras_posibles == []:
            return 'pass'
               
        else:
            if self.smartCoinFlip == True:
                pos = 0
                for lett in SORTED_FREQUENCIES:
                    if lett in letras_posibles:
                        pos = SORTED_FREQUENCIES.index(lett)
                
                return SORTED_FREQUENCIES[pos]
            else:
                return random.choice(letras_posibles)