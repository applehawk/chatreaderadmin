#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler, ButtonType, MenuButton
from config import *

choosed_theme = ""

class PaymentMethodMenu(BaseMessage):
    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)
        self.add_button(label='YooMoney', callback=None)
        # 'back' button goes back to previous menu
        self.add_button_back()
        self.add_button_home()

    def update(self) -> str:
        """Update message content."""
        return "Вы способ оплаты"

class SubscribtionPriceMenuSelection(BaseMessage):
    LABEL = ""

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)
        paymenu = PaymentMethodMenu(navigation)

        self.add_button(label='1 неделя за 1499 руб.', callback=paymenu)
        self.add_button(label='2 недели за 1999 руб.', callback=paymenu)
        self.add_button(label='1 месяц за 2999 руб.', callback=paymenu, new_row=True)
        self.add_button(label='3 месяца за 8089 руб.', callback=paymenu)
        self.add_button(label='6 месяцев за 15289 руб.', callback=paymenu)
        self.add_button(label='1 год за 28789 руб.', callback=paymenu)
        # 'back' button goes back to previous menu
        self.add_button_back()
        self.add_button_home()

    def update(self) -> str:
        """Update message content."""
        return "Выберите подписку"


class SubscribtionMenuSelectSubject(BaseMessage):
    LABEL = "💳 Оформить подписку"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)

        price_menu = SubscribtionPriceMenuSelection(navigation)
        self.add_button(label='Digital', callback=price_menu)
        self.add_button(label='Seo', callback=price_menu)
        self.add_button(label='Контекст', callback=price_menu, new_row=True)
        self.add_button(label='Таргет', callback=price_menu)
        # 'back' button goes back to previous menu
        self.add_button_back()

    def update(self) -> str:
        """Update message content."""
        return "Выберите тему"

class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    @staticmethod
    def goto_menu_callback() -> str:
        return "📱 Перейти в меню"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)
        subscribtion_menu = SubscribtionMenuSelectSubject(navigation)
        self.add_button(label="💳 Оформить подписку", callback=subscribtion_menu, btype=ButtonType.MESSAGE)
        self.add_button(label="📱 Перейти в меню", callback=self.goto_menu_callback, btype=ButtonType.PICTURE, new_row=True)

    def update(self) -> str:
        """Update message content."""
        return """📱 Главное меню 📱

Для выбора тематики и оплаты нажмите кнопку "💳 Оформить подписку".

Если клавиатура не видна, нажмите на иконку с четырьмя точками справа от поля ввода сообщения."""


def main() -> None:

    """Run the bot."""
    telegram_session = TelegramMenuSession(BOT_API_TOKEN)
    telegram_session.start(StartMessage)

if __name__ == '__main__':
    main()
