test_that("The right dummy message comes back.", {
  # Arrange
  expected_message <- "This is an R dummy."
  # Act
  returned_message <- dummy()
  # Assert
  expect_equal(returned_message, expected_message)
})
