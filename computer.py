class Computer:
    
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description,processor_type,hard_drive_capacity,memory,operating_system,year_made,price,computer_id,new_os):
        self.price=price
        self.computer_id=computer_id
        self.new_os=new_os
        self.description= description
        self.processor_type=processor_type
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made

         # You'll remove this when you fill out your constructor


    # What methods will you need?
    def __str__(self):
        """prints information as a dictionary
      """
        return str({'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price
})