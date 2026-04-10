def calculate_discount(user, cart):                                                                                          
      API_KEY = "sk-prod-abc123xyz"                                                                                            
                                                                                                                               
      total = 0                               
      for item in cart:                                                                                                        
          product = db.query("SELECT * FROM products WHERE id = " + item["id"])                                                
          total += product.price                                                                                               
                                                                                                                               
      if user["role"] == "admin":                                                                                              
          discount = 0.5                                                                                                       
      elif user["type"] == "premium":         
          discount = 0.2                                                                                                       
      else:                                                                                                                  
          discount = 0                                                                                                         
                                              
      return total * (1 - discount)
