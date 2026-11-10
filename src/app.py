import telebot 
import base
import app_api


bot = telebot.TeleBot(base.TOKEN)

print("bot created...")

# ================= START =================

@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        telebot.types.KeyboardButton("Search"),
        telebot.types.KeyboardButton("Popular"))
    
    markup.add(telebot.types.KeyboardButton("Help"))

    bot.send_message(message.chat.id,"🎬 Welcome to Movie Bot!\n\nChoose an option:",reply_markup=markup)

# ================= HELP =================

@bot.message_handler(commands=["help"])
def help_command(message):
    markup = telebot.types.ReplyKeyboardRemove()

    text = (
        """**Movie Bot Help**\n\n
Search:
Search for a movie by entering its name.\n
Popular:
See popular movies.\n
You can click on a movie to see more information.\n\n
Click on /start to see button again.
""")

    bot.send_message(message.chat.id,text,reply_markup=markup)

# ================= SEARCH =================

@bot.message_handler(commands=["search"])
def search_command(message):
    msg = bot.send_message(message.chat.id,"Please enter the movie name:")

    bot.register_next_step_handler(msg, search_movie)


def search_movie(message):
    movie_name = message.text.strip()

    if not movie_name:
        bot.send_message(message.chat.id, "Please enter a movie name.")
        return
        

    movies = app_api.search_movie(movie_name)

    if not movies:
        bot.send_message(message.chat.id,"❌ No movies found. Please try another name.")
        return
        

    keyboard = telebot.types.InlineKeyboardMarkup()

    for movie in movies:
        title = movie.get("Title", "Unknown")
        year = movie.get("Year", "")
        imdb_id = movie.get("imdbID")

        button = telebot.types.InlineKeyboardButton(f"{title} ({year})",callback_data=f"movie:{imdb_id}")
        keyboard.add(button)

    bot.send_message(message.chat.id,"🎬 Search results:",reply_markup=keyboard)

# ================= POPULAR =================

@bot.message_handler(commands=["popular"])
def popular_command(message):
    show_popular_movies(message)


def show_popular_movies(message):
    movies = app_api.get_popular_movies()

    if not movies:
        bot.send_message(message.chat.id, "❌ Could not get movie list.")
        return
        

    keyboard = telebot.types.InlineKeyboardMarkup()

    for movie in movies:
        title = movie.get("Title", "Unknown")
        year = movie.get("Year", "")
        imdb_id = movie.get("imdbID")

        button = telebot.types.InlineKeyboardButton(f"{title} ({year})",callback_data=f"movie:{imdb_id}")
        keyboard.add(button)

    bot.send_message(message.chat.id,"🔥 Popular movies:",reply_markup=keyboard)

# ================= MOVIE DETAILS =================

@bot.callback_query_handler(func=lambda call: call.data.startswith("movie:"))
def movie_details(call):
    imdb_id = call.data.split(":")[1]

    movie = app_api.get_movie_info(imdb_id)

    if not movie:
        bot.answer_callback_query(call.id,"Could not get movie information.")
        return
        
    title = movie.get("Title", "Unknown")
    year = movie.get("Year", "Unknown")
    rating = movie.get("imdbRating", "N/A")
    runtime = movie.get("Runtime", "N/A")
    genre = movie.get("Genre", "N/A")
    director = movie.get("Director", "N/A")
    actors = movie.get("Actors", "N/A")
    overview = movie.get("Plot", "No description available.")

    text = (
        f"🎬 <b>{title}</b>\n\n"
        f"📅 Year: {year}\n"
        f"⭐ IMDb Rating: {rating}\n"
        f"⏱ Runtime: {runtime}\n"
        f"🎭 Genre: {genre}\n"
        f"🎬 Director: {director}\n"
        f"👥 Actors: {actors}\n\n"
        f"📝 <b>Overview:</b>\n{overview}")

    bot.answer_callback_query(call.id)

    bot.send_message(call.message.chat.id,text,parse_mode="HTML")

# ================= OTHER MESSAGE =================

@bot.message_handler(func=lambda message:True)
def other_message(message):
    if message.text == "Search":
        search_command(message)

    elif message.text == "Popular":
        show_popular_movies(message)

    elif message.text == "Help":
        help_command(message)

    else:
        bot.send_message(message.chat.id,"Please choose one of the buttons.")

# ==================================

if __name__ == "__main__":
    bot.infinity_polling()