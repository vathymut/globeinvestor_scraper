# Merge all csv files containing the rates
#
# Author: Vathy M. Kamulete (Bank of Canada)

rm( list=ls( all.names = T ) )
options(scipen=20)              ## Sets decimal places  scientific notation
options(prompt="R> ")           ## Changes the prompt to R>
options(digits=2)
graphics.off()

#### Change directory ####
setwd( 'B:/scraping_rates_jason/' )

#### Get libraries ####
pkgs <- c( 'data.table', 'stringr', 'lubridate' )
lapply( pkgs, require, character.only = TRUE )

#### Create function to merge CSV Files ####
concatCsv <- function( vecCsvFilenames ){
  # vecCsvFilenames, csv filenames to merge
  dtList <- list()
  patternToRemove <- "-\\d+-\\d+-\\d+.csv$" # Strip date and file extension
  for ( idx in 1:length( vecCsvFilenames ) ){
    rates_type <- str_replace_all( csvFiles[idx], pattern = patternToRemove, replacement = "" )
    dt <- read.csv( csvFiles[idx], stringsAsFactors = FALSE, header = TRUE )
    setDT( dt ) # Convert to data.table
    dt[ , rates_type := rates_type ] # Add rates_type to dataset
    dtList[[ idx ]] <- dt
  }
  return( rbindlist( dtList, fill = TRUE ) )
}

#### Merge all csv files ####
csvFiles <- list.files( ".", "*.csv" )
# Remove file containing 'AllScrapedRates'
selectedFiles <- csvFiles[ !str_detect( csvFiles, "AllScrapedRates-" ) ]
# Merge files
rates <- concatCsv( selectedFiles )
# Rename columns
oldNames <- c( "X30days", "X60days", "X90days", "X120days", "X180days", "X270days" )
newNames <- c( "days30", "days60", "days90", "days120", "days180", "days270" )
setnames( rates, oldNames, newNames  )
rm( oldNames, newNames )

#### Save dataset ####
todayAsString <- as.character( today() )
fileName <- str_c( "AllScrapedRates-", todayAsString, ".csv"   )
write.csv( rates, file = fileName, row.names = FALSE )

#### Delete csv files when done ####
file.remove( selectedFiles ) 
