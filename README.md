# Flashy Flashcard App

**Flashy** is a versatile flashcard application built using Python and the Tkinter library. It enables you to create and automatically flip flashcards for any purpose, whether it's learning a new language, studying facts, or memorizing information. With Flashy, you can customize the content on both sides of the flashcards to suit your specific needs.

## Features

- Automatic Flipping: Flashcards automatically flip to reveal the answer after 3 seconds.
- Content Customization: Customize the content of `original_flashcards.csv` with any information you want to learn.
- Easy Navigation: Move to the next flashcard with a simple click.
- Progress Tracking: Track your progress as you review and mark cards as "known." The app creates a separate `flashcards_to_learn.csv` to track your progress.
- Data Persistence: Your flashcards and learning progress are saved in CSV files for future use.

## Getting Started

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/flashy-flashcard-app.git
   ```

2. Install the required Python libraries (if not already installed):

   ```bash
   pip install pandas
   ```

3. Modify the `original_flashcards.csv` file to include your content on both sides of the flashcards. Add your flashcards at the start.

4. Run the app:

   ```bash
   python flashcard.py
   ```

## Usage

1. The app starts by displaying the content on the front of the flashcard.

2. After 3 seconds, the flashcard automatically flips to reveal the content on the back.

3. Click the checkmark if you knew the information or the cross if you didn't.

4. If you click the checkmark, the flashcard is marked as "known," and the app proceeds to the next flashcard.

5. If you click the cross, the flashcard remains in the "to learn" set, and the app proceeds to the next flashcard.

6. The learning progress is saved in the `flashcards_to_learn.csv`, and you can continue learning from where you left off.

## Customization

Flashy allows you to create and study flashcards for any topic. You can customize the content in `original_flashcards.csv`. However, the `flashcards_to_learn.csv` is automatically generated and tracks your learning progress.

To customize flashcards:

1. Modify the `original_flashcards.csv` file to include your content on both sides of the flashcards.

2. When you run the app, it will load your customized flashcards for you to study.
