import streamlit as st
import random

# Game Rules
st.title("🧙‍♂️⚔️🐉 Wizard, Warrior, Dragon")

st.markdown("""
## 🧩 Game Rules

- **Wizard** defeats **Dragon**
- **Warrior** defeats **Wizard**
- **Dragon** defeats **Warrior**

**It's like Rock, Paper, Scissors — but more magical!**
""")

# ASCII Art
wizard = '''
       /^\\
      /   \\
     |  o o|
     |  (_)| 
      \\___/
     _|_|_|_
    /       \\
   /|       |\\
  /_|_______|_\\
    |  | |  |
    |__|_|__|
'''

warrior = '''
     ,^.
    // \\\\
   || * ||
   ||___||
   |  |  |
  /|  |  |\\
 ( |  |  | )
  |__|_|__|
    /   \\
   (_____)
    | |
    | |
   /___\\
'''

dragon = '''
               /           /
              /' .,,,,  ./
             /';'     ,/
            / /   ,,//,`'`
           ( ,, '_,  ,,,' \\
           |    /@  ,,, ;" \\
          /    .   ,''/' \\   )
         /   .     ./, `,,/
      ,./  .   ,-,',`  '
     |   /; ./,,'`,''\\
     |     /   ','    \\
      \\___/'   '     |
        `,,'  |      /
             |     /
              `---'
'''

choices = ["Wizard", "Warrior", "Dragon"]
ascii_art = [wizard, warrior, dragon]

# User selection
user_choice = st.radio("Choose your champion:", choices)

if st.button("Battle!"):
    user_index = choices.index(user_choice)
    computer_index = random.randint(0, 2)

    # Show selections
    st.subheader("🧑‍💻 You chose:")
    st.code(ascii_art[user_index])

    st.subheader("💻 Computer chose:")
    st.code(ascii_art[computer_index])

    # Game Logic
    if user_index == computer_index:
        st.info("It's a draw!")
    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        st.success("You win!")
    else:
        st.error("You lose!")
