#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler, ButtonType, MenuButton
from config import *

#choosed_theme = ""

class SharedState():
    def __init__(self):
        self.choosed_subscribtion: str = ""
        self.choosed_subject: str = ""

class PaymentMethodMenu(BaseMessage):
    LABEL = "Способ оплаты"
    def __init__(self, navigation: NavigationHandler, shared: SharedState) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, PaymentMethodMenu.LABEL)

        self.shared = shared

        self.add_button(label='YooMoney', callback=None)
        # 'back' button goes back to previous menu
        self.add_button_back()
        self.add_button_home()

    def update(self) -> str:
        """Update message content."""
        return f"""Вы выбрали подписку: {self.shared.choosed_subscribtion} и тему: {self.shared.choosed_subject}
        
Выберите способ оплаты:
        """

class SubscribtionPriceMenuSelection(BaseMessage):
    LABEL = "Выбрать подписку"
    
    def __init__(self, navigation: NavigationHandler, shared: SharedState) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, SubscribtionPriceMenuSelection.LABEL)
        self.paymenu = PaymentMethodMenu(navigation, shared)
        self.shared = shared

        paymenu = self.paymenu

        self.add_button(label='1 неделя за 1499 руб.')
        self.add_button(label='2 недели за 1999 руб.')
        self.add_button(label='1 месяц за 2999 руб.', new_row=True)
        self.add_button(label='3 месяца за 8089 руб.')
        self.add_button(label='6 месяцев за 15289 руб.')
        self.add_button(label='1 год за 28789 руб.')

        self.add_button(PaymentMethodMenu.LABEL, self.paymenu)
        # 'back' button goes back to previous menu
        self.add_button_back()
        self.add_button_home()

    def text_input(self, text: str) -> None:
        self.shared.choosed_subscribtion = text
        self._navigation.select_menu_button(PaymentMethodMenu.LABEL)

    def update(self) -> str:
        content = f"{self.shared.choosed_subject}" if self.shared.choosed_subject else ""
        return f"Вы выбрали: {content} Выберите подписку"


class SubscribtionMenuSelectSubject(BaseMessage):
    LABEL = "💳 Оформить подписку"

    def __init__(self, navigation: NavigationHandler, shared: SharedState) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, SubscribtionMenuSelectSubject.LABEL)
        self.shared = shared
        self.price_menu = SubscribtionPriceMenuSelection(navigation, shared)

        self.add_button('Digital')
        self.add_button('Seo')
        self.add_button('Контекст', new_row=True)
        self.add_button('Таргет')
        self.add_button(SubscribtionPriceMenuSelection.LABEL, self.price_menu)
        # 'back' button goes back to previous menu
        self.add_button_back()

    def text_input(self, text: str) -> None:
        self.shared.choosed_subject = text
        self._navigation.select_menu_button(SubscribtionPriceMenuSelection.LABEL)

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
        shared = SharedState()
        subscribtion_menu = SubscribtionMenuSelectSubject(navigation, shared=shared)
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
