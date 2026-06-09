from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Начальный список блюд
DEFAULT_MEALS = ['Борщ', 'Пельмени', 'Гречка с котлетой', 'Омлет', 'Салат Цезарь']

# В реальном проекте здесь будет база данных
# Пока храним в словаре (проще для понимания)
meals_storage = {}


@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')


@app.route('/api/get_meals', methods=['GET'])
def get_meals():
    """Получить список блюд для пользователя"""
    # В реальном проекте здесь будет идентификация пользователя
    # Пока используем заглушку - всегда возвращаем DEFAULT_MEALS
    return jsonify(DEFAULT_MEALS)


@app.route('/api/add_meal', methods=['POST'])
def add_meal():
    """Добавить новое блюдо"""
    data = request.get_json()
    meal = data.get('meal', '').strip()

    if not meal:
        return jsonify({'error': 'Название блюда не может быть пустым'}), 400

    # В реальном проекте здесь сохранение в БД
    DEFAULT_MEALS.append(meal)

    return jsonify({'success': True, 'meals': DEFAULT_MEALS})


@app.route('/api/delete_meal', methods=['POST'])
def delete_meal():
    """Удалить блюдо по индексу"""
    data = request.get_json()
    index = data.get('index')

    if index is None or index < 0 or index >= len(DEFAULT_MEALS):
        return jsonify({'error': 'Неверный индекс'}), 400

    deleted = DEFAULT_MEALS.pop(index)

    return jsonify({'success': True, 'deleted': deleted, 'meals': DEFAULT_MEALS})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)