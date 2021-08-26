shinyServer(function(input, output) {

  output$plot <- renderPlot({
    heart_convert %>%
      ggplot(aes(x = !!input$x_axis, y = cp))+
      geom_point()
  })
  # The if else statement was not present in the original DQ instructions; this is SUPER important to include, otherwise you won't be able to hide the data with the checkbox input
  output$user_data <- renderDataTable({
    if (input$wants_table == TRUE){
        heart_convert
    } else {
      
    }
  })
})
