from abc import ABC, abstractmethod


class SocialNetwork(ABC):
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, users: int, active_users: int):
        """
        Аргументы:
            name (str): Название социальной сети.
            users (int):  Общее количество пользователей в социальной сети.
            active_users (int): Количество активных пользователей в социальной сети.
        """
        self.name = name
        self.users = users
        self.active_users = active_users

    @abstractmethod
    def post(self, content: str) -> str:
        """
        Опубликовать контент в социальной сети.


        Аргументы:
            content (str): Контент для публикации

        Returns:
            str: Сообщение об успешной публикации.
        """
        pass

    @abstractmethod
    def like(self, post_id: int) -> str:
        """
        Поставить лайк посту в социальной сети.

        Args:
            post_id (int): ID поста, который нужно лайкнуть.

        Returns:
            str: Сообщение об успешном действии лайка.
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Returns:
            str: Строковое представление социальной сети.
        """
        return f"{self.name} - Всего пользователей: {self.users},  Активные пользователи: {self.active_users}"

    def __repr__(self) -> str:
        """
         Возвращает строковое представление социальной сети для отладки.

        Returns:
            str: Строковое представление социальной сети.
        """
        return f"{self.__class__.__name__}(Имя={self.name}, Пользователи={self.users}, Активные пользователи={self.active_users})"


class VK(SocialNetwork):
    """Класс, представляющий социальную сеть ВКонтакте."""

    def __init__(self, name: str, users: int, active_users: int, groups: int):
        """
        Args:
            name (str): Название социальной сети.
            users (int): Общее количество пользователей в социальной сети.
            active_users (int): Количество активных пользователей в социальной сети.
            groups (int): Общее количество групп в социальной сети ВКонтакте.
        """
        super().__init__(name, users, active_users)
        self.groups = groups

    def post(self, content: str) -> str:
        """
         Опубликовать контент в ВК.

        Args:
            content (str): Контент для публикации.

        Returns:
            str: Сообщение об успешной публикации.
        """
        return f"Опубликовано '{content}' в ВКонтакте."

    def like(self, post_id: int) -> str:
        """
        Поставить лайк посту в ВКонтакте.

        Args:
            post_id (int): ID поста, который нужно лайкнуть.

        Returns:
            str: Сообщение об успешном действии лайка.
        """
        return f"Поставлен лайк посту с ID {post_id} в ВКонтакте."


if __name__ == "__main__":
    vk = VK("ВКонтакте", 100000, 80000000, 1000000)
    print(vk)
    print(repr(vk))

    print(vk.post("Hello, VK!"))
    print(vk.like(123456))