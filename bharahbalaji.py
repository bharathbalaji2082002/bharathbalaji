
import random

# Collection of quotes for each category
quotes = {
    'motivation': [
        "Believe it is possible, {name}. The only way to achieve the impossible is to believe.",
        "Success is not final, {name}. Failure is not fatal: It is the courage to continue that counts.",
        "Don't waste it living someone else's life, {name}. Your time is limited, don't waste it.",
        "Keep going, {name}. Don't watch the clock; do what it does. Keep going.",
        "The harder you work for something, {name}, the greater you'll feel when you achieve it.",
        "Your future is created by what you do today, {name}, not tomorrow.",
        "Success doesn't come from what you do occasionally, {name}, but what you do consistently."
    ],
    'success': [
        "Success is not in what you have, {name}, but who you are.",
        "The secret to success, {name}, is to know something nobody else knows.",
        "Success is not about the destination, {name}, but the journey.",
        "Success usually comes to those who are too busy to be looking for it, {name}.",
        "The road to success and the road to failure are almost exactly the same, {name}.",
        "Success is not just about making money, {name}; it's about making a difference.",
        "The successful warrior is the average man, {name}, with laser-like focus."
    ],
    'life': [
        "Life is what happens when you're busy making other plans, {name}.",
        "Life is 10% what happens to us, {name}, and 90% how we react to it.",
        "Make it amazing, {name}. Life is short, make it amazing.",
        "In the end, {name}, it's not the years in your life that count. It's the life in your years.",
        "The purpose of our lives is to be happy, {name}.",
        "Life is like riding a bicycle, {name}. To keep your balance, you must keep moving.",
        "Life is not a problem to be solved, {name}, but a reality to be experienced."
    ],
    'love': [
        "Hold onto each other, {name}. The best thing to hold onto in life is each other.",
        "Love each other every single day, {name}. Love is not about how many days, months, or years you have been together.",
        "Endless forgiveness, {name}. Love is an endless act of forgiveness.",
        "Love is when the other person's happiness is more important than your own, {name}.",
        "Being deeply loved by someone gives you strength, {name}, while loving someone deeply gives you courage.",
        "The greatest happiness you can have is knowing that you do not necessarily require happiness, {name}.",
        "Love is not finding someone to live with, {name}, but finding someone you can't live without."
    ],
    'inspiration': [
        "Realize tomorrow, {name}. The only limit to our realization of tomorrow will be our doubts of today.",
        "Invent your future, {name}. The best way to predict the future is to invent it.",
        "Work for success, {name}. The only place where success comes before work is in the dictionary.",
        "Lift up someone else, {name}. If you want to lift yourself up, lift up someone else.",
        "The only thing standing between you and your goal, {name}, is the story you keep telling yourself.",
        "I can't change the direction of the wind, {name}, but I can adjust my sails to always reach my destination.",
        "Don't let yesterday take up too much of today, {name}."
    ],
    'wisdom': [
        "Know you know nothing, {name}. The only true wisdom is in knowing you know nothing.",
        "Have sight and vision, {name}. The only thing worse than being blind is having sight but no vision.",
        "Observe and acquire wisdom, {name}. To acquire knowledge, one must study; but to acquire wisdom, one must observe.",
        "It is the mark of an educated mind, {name}, to be able to entertain a thought without accepting it.",
        "The more I learn, {name}, the more I realize how much I don't know.",
        "The only wisdom is knowing you know nothing, {name}.",
        "Life is too important to be taken seriously, {name}."
    ]
}

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input

def get_random_quote(category):
    quotes_for_category = quotes.get(category.lower())
    if not quotes_for_category:
        return None
    return random.choice(quotes_for_category)

def main():
    print("Welcome to the Quote Generator!")
    name = get_user_input("Please enter your name: ")
    categories = list(quotes.keys())

    while True:
        category_prompt = f"Select a category for the quote ({', '.join(categories)}): "
        while True:
            selected_category = get_user_input(category_prompt)
            selected_category = selected_category.lower()
            if selected_category in categories:
                break
            print("Invalid category, please try again.")

        quote = get_random_quote(selected_category)
        if quote:
            personalized_quote = quote.replace('{name}', name)
            print("Here's your personalized quote:")
            print(personalized_quote)
        else:
            print("Sorry, there are no quotes available for the selected category.")

        try_again = input("Would you like to try another quote? (yes/no): ").strip().lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()
