from __future__ import annotations
from abc import ABC, abstractmethod


class TemplateClass(ABC):

    def template_method(self) -> None:
        self.base_operation_1()
        self.required_subclass_operation_1()
        self.base_operation_2()
        self.hook_1()
        self.required_subclass_operation_2()
        self.base_operation_3()
        self.hook_2()

    def base_operation_1(self) -> None:
        print("Template class does bulk of the work in step 1.")

    def base_operation_2(self) -> None:
        print("In step 2, Template class continues doing bulk of the work. Some methods can be overriden by subclasses.")

    def base_operation_3(self) -> None:
        print("Template class finished bulk of the work in step 3.")

    @abstractmethod
    # Method below needs to be overriden by a subclass.
    def required_subclass_operation_1(self) -> None:
        pass

    @abstractmethod
    # Method below needs to be overriden by a subclass.
    def required_subclass_operation_2(self) -> None:
        pass

    def hook_1(self) -> None:
        """
        Hooks are optional. It allows subclasses to add additional code in key places of the algorithm
        """
        pass

    def hook_2(self) -> None:
        pass


if __name__ == "__main__":
    pass
