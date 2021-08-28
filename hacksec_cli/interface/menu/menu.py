from PyInquirer import style_from_dict, Token, prompt, Separator

MENU = ["Overview", "active weblab", "retired weblab", "upcoming weblab",
        "report", "profile", "team", "announcement", "activity", "ranking", "settings", "premium", "Help", "About"]

style = style_from_dict({
    Token.Separator: '#008060 bold',
    Token.QuestionMark: '#008060 bold',
    Token.Selected: '#008060',  # default
    Token.Pointer: '#008060 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#008060 bold',
    Token.Question: '#008060 bold',
})


def main_menu():
    Menu_items = [Separator('= Main Menu =')]
    for i in MENU:
        if i == "premium":
            Menu_items.append({"name": i, 'disabled': 'coming soon'})
        else:
            Menu_items.append({"name": i})
    questions = [
        {
            'type': 'list',
            'message': 'Please select an option',
            'name': 'menu',
            'choices': Menu_items,
        }
    ]
    answers = prompt(questions, style=style)
    if len(answers) == 0:
        return None
    return answers["menu"]
