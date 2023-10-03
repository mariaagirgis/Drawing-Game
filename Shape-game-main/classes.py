

class Drawing:

    
    def __init__(self, name, actualPoints, userPoints):

        #initializes variables for use in class
        self.name = name
        self.userPoints = userPoints
        self.actualPoints = actualPoints

    
    def imagePath(self):        #returns image path
        return 'images/' + self.name + '.gif'

    #method to determine percentage accuracy
    
    def grade(self):

        #empty list to store all the point variances 
        diffVals = []

        #for loop that calculates each difference percentage for each list of numbers
        for i in range(len(self.userPoints)):
            
            difference = 0
            
            for j in range(4):
        
                #for each point in the array of 4 numbers, calulcate the difference between the user and actual points
                
                lineDiff = abs(self.userPoints[i][j]-170 - self.actualPoints[i][j])
                difference = difference + lineDiff

                #for loop that removes all numbers that would lead to negative percent
                if difference >= 100:
                    difference = 100

                    
            diffVals.append(difference)
                
        #calculates average of all nums in diffVal list
        def Average(lst):
            return sum(lst) / len(lst)

        #calculates average difference percent and rounds
        averageDiff = round(Average(diffVals))

        #error catching for negative numbers
        if 100 - averageDiff < 0:
            return '0%'

        else:
            #returns the average diff as a percent
            return (str(100 - averageDiff) + '%')

        

            


            
                
            

            
                

                
            


                

    

    

