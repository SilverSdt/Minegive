class IntRange:
    """Represents a range of integers."""

    def __init__(self, start: int | None = None, end: int | None = None):
        """Initializes a new instance of the IntRange class. Start and end cannot be None at the same time.
        If start is None, the range is from -infinity to end.
        If end is None, the range is from start to +infinity.

        Args:
            start (int | None, optional): Start of the range. Defaults to None.
            end (int | None, optional): End of the range. Defaults to None.
        """
        if start is None and end is None:
            raise ValueError("Invalid range")
        self._start = start
        self._end = end

    @property
    def start(self) -> int | None:
        """Start of the range."""
        return self._start

    @property
    def end(self) -> int | None:
        """End of the range."""
        return self._end

    @start.setter
    def start(self, value: int | None):
        """Start of the range."""
        if value is None and self._end is None:
            raise ValueError("Invalid range")
        self._start = value

    @end.setter
    def end(self, value: int | None):
        """End of the range."""
        if value is None and self._start is None:
            raise ValueError("Invalid range")
        self._end = value

    def __str__(self) -> str:
        """Returns a string representation of the range.

        Raises:
            ValueError: Invalid range.

        Returns:
            str: String representation of the range.
        """
        if self._start is None and self._end is None:
            raise ValueError("Invalid range")
        elif self._start is None:
            return f"..{self._end}"
        elif self._end is None:
            return f"{self._start}.."
        return f"{self._start}..{self._end}"
