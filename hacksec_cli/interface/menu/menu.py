from PyInquirer import style_from_dict, Token, prompt, Separator

style = style_from_dict({
    Token.Separator: '#008060 bold',
    Token.QuestionMark: '#008060 bold',
    Token.Selected: '#008060',  # default
    Token.Pointer: '#008060 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#008060 bold',
    Token.Question: '#008060 bold',
})


MENU = ["Overview", "Active weblab", "Retired weblab", "Upcoming weblab",
        "Report", "Profile", "Team", "Announcement", "Activity", "Ranking", "Settings", "Help", "About", "Contact us", "Logout", "Premium", "Tools"]


def main_menu(menu_name="Main Menu", MenuList=None, discription=None):
    if discription == None:
        discription = "Select an option"
    Menu_items = [Separator('= '+menu_name+' =')]
    if MenuList is None:
        for i in MENU:
            if i.lower() == "premium" or i.lower() == "tools":
                Menu_items.append({"name": i, 'disabled': 'coming soon'})
            else:
                Menu_items.append({"name": i})
    else:
        for i in MenuList:
            Menu_items.append({"name": i})
    questions = [
        {
            'type': 'list',
            'message': discription,
            'name': 'menu',
            'choices': Menu_items,
        }
    ]
    answers = prompt(questions, style=style)
    if len(answers) == 0:
        return None
    return answers["menu"].lower()
