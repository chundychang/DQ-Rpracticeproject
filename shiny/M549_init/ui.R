# This data dashboard should have the following interface:
# - Choose columns to place on the x- and y-axis of a plot
# - Filter the data down to specific values
# - Choose a column to group on
# - Show what the underlying data looks like to the user
# - Visualize the data as an informative plot to the user

shinyUI(navbarPage(
    title = "DQ Dashboard",
    theme = "styles.css",
    tabPanel(title = "Home",
             img(
                 src="splash-photo.jpg",
                 width="100%"
             ),
             h1("About This App"),
             p("Explore how different factors influence heart conditions by toggling the settings yourself.")),
    tabPanel(title = "Dashboard", sidebarLayout(
        sidebarPanel(
            varSelectInput(
                inputId = "x_axis",
                label = "Choose a column from the data:",
                data = heart_convert
            ),
            checkboxInput(
                inputId = "wants_group",
                label = "Enable grouping?:",
                value = FALSE
            ),
            varSelectInput(
                inputId = "group_col",
                label = "Choose a column to group on:",
                data = heart_convert
            ),
            checkboxInput(
                inputId = "wants_table",
                label = "Show underlying data?",
                value = FALSE
            )
        ),
        mainPanel(
            plotOutput("plot"),
            conditionalPanel(
                condition = "input.wants_table == TRUE",
                dataTableOutput("user_data")
            )),
    
    # 459.4: Coding The Main Layout
    # In the lines below, give the user interface a sidebarLayout
    
    )
)))