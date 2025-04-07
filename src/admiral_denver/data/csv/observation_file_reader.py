"""Iterate through a survey data file."""


class ObservationFileReader:
    """Iterate through a survey data file."""

    def __init__(self, file_path: str) -> None:
        """Initialize with the survey file path."""
        # Open the file on initialization and ensure there are no records yet.
        self.file = open(file_path, "r", encoding="utf-8")
        self.current_record: str | None = None
        self.next_line: str | None = None  # So we can read ahead.

    def __iter__(self):
        return self

    def __next__(self) -> str:
        """Return the next record in the file."""
        # If there is no record go and get it.
        if self.current_record is None:
            self.current_record = self._read_record()
        # Create a record to return or stop.
        record = self.current_record
        if record is None:  # we are at the end of the file.
            self.file.close()
            raise StopIteration
        self.current_record = None  # Reset current record for next iteration.
        return record

    def _read_record(self) -> str | None:
        """Read from the file to the end of the species list."""
        record_lines = ""
        in_species = False  # The species list is the last field in the record.
        # If there is a line from the next record, add it to the record lines.
        if self.next_line and self._get_field(self.next_line):
            record_lines += self.next_line
        for line in self.file:
            self.next_line = line  # Keep line in case it's needed for next record.
            # The species list is the last field in the record.
            field = self._get_field(line)
            if field != "species" and in_species and field:
                break  # We have reached the end of the record.
            elif field != "species":
                record_lines += line  # Append another field or species line.
            else:  # We have reached the species list.
                record_lines += line
                in_species = True
        # Return the lines or close and finish.
        if record_lines:
            return record_lines
        self.file.close()
        return None

    def _get_field(self, line):
        """Return the field name from the line."""
        field_name, _ = line.split(",", 1)
        field_name = field_name.strip()
        return field_name
