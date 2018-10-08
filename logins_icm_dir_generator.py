#!/usr/bin/env python
import random

names_list = [
"Dangelo Hurley    ",
"Chris Mann",
"Clark Barber      ",
"Dominique Miles   ",
"Alvin Flowers     ",
"Kinley Burton     ",
"Cailyn Chang      ",
"Jovani Nicholson  ",
"Anthony Sweeney   ",
"Sam Buchanan      ",
"Annie Nelson      ",
"Zayne Boyle       ",
"Yadira Newman     ",
"Skyler Hicks      ",
"Meredith Dalton   ",
"Francis Gomez     ",
"Leilani Byrd      ",
"Solomon Morrison  ",
"Kiley Singleton   ",
"Mareli Juarez     ",
"Destiney Crane    ",
"Jay Pruitt",
"Cayden Vance      ",
"Ellis Frazier     ",
"Julissa Gilbert   ",
"Elise Gill",
"Harper Keith      ",
"Ariel Francis     ",
"Aydan Heath       ",
"Jazmine Harrington",
"Grayson Young     ",
"Savion Herman     ",
"Kennedy Adkins    ",
"Jaslyn Bass       ",
"Elisha Farrell    ",
"Orlando Hogan     ",
"Roselyn Mccann    ",
"Sariah Blankenship",
"Beau Andrade      ",
"Darius Berger     ",
"Selena Davies     ",
"Lyric Ferrell     ",
"Jasiah Mack       ",
"Liana Navarro     ",
"Aydin Mcgrath     ",
"Jada Conway       ",
"Amiyah Bray       ",
"Tia Sexton",
"Monique Robinson  ",
"Carlos Marsh      ",
"Haley Rose",
"Dakota Copeland   ",
"Edwin Ramsey      ",
"Yareli Little     ",
"Ruth Roy  ",
"Riya Calhoun      ",
"Nathan Briggs     ",
"Lucy Harris       ",
"Jeffery Daniels   ",
"Deja Mata ",
"Nylah Suarez      ",
"Ryan Avila",
"Haylee Glass      ",
"Riley Beck",
"Colby Campos      ",
"Kieran Vazquez    ",
"Omari Trevino     ",
"Madelyn Costa     ",
"Van Finley",
"Randy Carpenter   ",
"Devin Acosta      ",
"Nyla Cunningham   ",
"Alden Moore       ",
"Sarahi Soto       ",
"Shyla Wilkins     ",
"Sofia Lindsey     ",
"Ada Stanley       ",
"Kristin Villarreal",
"Maurice Bowman    ",
"Casey Murphy      ",
"Abagail Sawyer    ",
"Jefferson Malone  ",
"Colin Santana     ",
"Hudson Orozco     ",
"Eden Nichols      ",
"Lilia Holland     ",
"Reese Shaffer     ",
"Marilyn Hardy     ",
"Harrison Nunez    ",
"Olivia Cummings   ",
"Aidyn Goodwin     ",
"Royce Pratt       ",
"Corbin Mcgee      ",
"Liliana Ali       ",
"Thaddeus Reyes    ",
"Jakob Richards    ",
"Sylvia Hayden     ",
"Adrian Newton     ",
"Amaris Sellers    ",
"Leslie Watts      ",
"Jamya Fox ",
"Arielle Mcfarland ",
"Kimberly Kirk     ",
"Alanna Velez      ",
"Emily Medina      ",
"Ashlyn Solomon    ",
"Tony Russell      ",
"Ronin Hampton     ",
"Kamryn Shelton    ",
"Connor Roach      ",
"Marie Massey      ",
"Jaydon Reilly     ",
"Ricardo Acevedo   ",
"Matthias Riddle   ",
"Peyton Doyle      ",
"Nayeli Berry      ",
"Hailie Hendricks  ",
"Jayden Meadows    ",
"Jaycee Michael    ",
"Summer Cannon     ",
"Armani Reid       ",
"Jazmyn Rhodes     ",
"Madyson Day       ",
"Gary Everett      ",
"Thalia Miller     ",
"Allisson Cherry   ",
"Elian Donaldson   ",
"Braxton Johnson   ",
"Bruce Andrews     ",
"Zechariah Garner  ",
"Kaleb Haynes      ",
"Isabella Oconnor  ",
"Trinity Morris    ",
"Jamar Larson      ",
"Carson Meza       ",
"Clayton Cervantes ",
"Todd Wiggins      ",
"Keaton Henry      ",
"Cannon Walls      ",
"Julio Mitchell    ",
"Chace Poole       ",
"Eliza Douglas     ",
"Campbell Camacho  ",
"Jorden Hutchinson ",
"Rhys Bradshaw     ",
"Kymani Bailey     ",
"Geovanni Rice     ",
"Alexis Good       ",
"Haven Galloway    ",
"Miguel Diaz       ",
"Armani Tucker     ",
"Ralph Barker      ",
"Aileen Archer     ",
"Cali Schroeder    ",
"Julianne Nolan    ",
"Ray Macdonald     ",
"Asher Simmons     ",
"Myles Holloway    ",
"Marlee Cox",
"Brendon Tyler     ",
"Jessie Harrell    ",
"Danica Best       ",
"Mathew Fisher     ",
"Abril Oneal       ",
"Gabriela Wagner   ",
"Javier Blanchard  ",
"Owen Page ",
"Noemi Gardner     ",
"Johanna Perkins   ",
"Kenyon Avery      ",
"Madden Daugherty  ",
"Alice Bradford    ",
"Leon Vaughn       ",
"Maci Hooper       ",
"Rachael Irwin     ",
"Alyson Lynn       ",
"Brisa Gillespie   ",
"Magdalena Weeks   ",
"Donovan Santiago  ",
"Daniella Maxwell  ",
"Colton Schmidt    ",
"Deshawn Lawrence  ",
"Myah Parsons      ",
"Dahlia Adams      ",
"Keira Mckinney    ",
"Calvin Mullen     ",
"Braiden Mora      ",
"Paola Mayer       ",
"Koen Burch",
"Brady Cooke       ",
"Evan Bean ",
"Emilia Molina     ",
"Makena Yoder      ",
"Kade Jimenez      ",
"Savannah Chung    ",
"Elliot Erickson   ",
"Natasha Ponce     ",
"Titus Atkins      ",
"Iyana Benitez     ",
"Lawson Compton    ",
"Silas Ellison     ",
"Amaya Church      ",
"Brennan Gilmore   ",
"Charity Fuentes   ",
"Darnell Kaufman   ",
"Brooke Wallace    ",
"Lucille Paul      ",
"Giada Winters     ",
"Deangelo Hebert   ",
"Ernest Hurst      ",
"Colten Fletcher   ",
"Celia Richard     ",
"Tamia Rosales     ",
"Nathanael Martin  ",
"Jase Summers      ",
"Sean Montes       ",
"Cynthia Schaefer  ",
"Kamren Roth       ",
"Brayden Harvey    ",
"Taylor Jacobs     ",
"Trevin Odonnell   ",
"Daniela Rivas     ",
"Fabian Whitehead  ",
"Yael Mayo ",
"Patricia Stokes   ",
"Ashlynn Key       ",
"Bryan Steele      ",
"Pedro Nash",
"Cassidy Frederick ",
"Anne Huang",
"Rory Stevens      ",
"Anton Baird       ",
"Hanna Murray      ",
"Sydney Hill       ",
"Coleman Kent      ",
"Miley Murillo     ",
"Tommy Cole",
"Arely Davila      ",
"Wesley Harrison   ",
"Sullivan Savage   ",
"Damien Mays       ",
"Mckayla Schmitt   ",
"Cora Jennings     ",
"Nathalie Escobar  ",
"Sara Campbell     ",
"Mackenzie Whitney ",
"Payton Conrad     ",
"Paris Washington  ",
"Santos Peterson   ",
"Fiona Lawson      ",
"Karley Alvarez    ",
"Rylee Strong      ",
"Haiden Jenkins    ",
"Shannon Ewing     ",
"Izabella Cantu    ",
"Avery Carson      ",
"Wade Howard       ",
"Jaxson Craig      ",
"Jerome Pierce     ",
"Heaven Jensen     ",
"Chloe Perry       ",
"Jaxon Bridges     ",
"Alma Castro       ",
"Yurem Green       ",
"Ean Proctor       ",
"Angela Duarte     ",
"Sierra Kelley     ",
"Karter Stark      ",
"Alexia Waller     ",
"Alfredo Short     ",
"Declan Leon       ",
"Eugene Rasmussen  ",
"Rebecca Cooper    ",
"Yandel Cowan      ",
"Jillian Huynh     ",
"Alex Harmon       ",
"Michaela Flores   ",
"Jamison Hudson    ",
"Landen Rubio      ",
"Micah Ho  ",
"Zaria Reese       ",
"Haleigh Herrera   ",
"Olive Park",
"Alondra Phillips  ",
"Yazmin Norris     ",
"Courtney King     ",
"Carlo Figueroa    ",
"Felicity Chaney   ",
"Terrell Mcmillan  ",
"Kallie Chen       ",
"Zachary Miranda   ",
"Alfred Long       ",
"Lauryn Neal       ",
"Emmalee Grimes    ",
"Izabelle Duke     ",
"Giovanny Salazar  ",
"Quinn Haney       ",
"Addisyn Hodges    ",
"Adrien Alexander  ",
"Anika Hunter      ",
"Makenzie Stuart   ",
"Maggie Peters     ",
"Terrence Pena     ",
"Bronson Rush      ",
"Anabella Mcdonald ",
"Cade Mccarthy     ",
"Janelle Scott     ",
"Dana Dixon",
"Laura Caldwell    ",
"Lilianna Parks    ",
"Heidi Hickman     ",
"Jeramiah Cortez   ",
"Kayley Ballard    ",
"Trent House       ",
"Raul Bond ",
"Bennett Marks     ",
"Leandro Hess      ",
"Howard Marquez    ",
"Cindy Lewis       ",
"Peter Wong",
"Lawrence Gates    ",
"Esteban Fuller    ",
"Kiersten Hamilton ",
"Stacy Bryan       ",
"Xzavier Ashley    ",
"Belen Wu  ",
"Brenton Bruce     ",
"Ashanti Hendrix   ",
"Amber Martinez    ",
"Frida Stout       ",
"Cloe Roman",
"Andrew Flynn      ",
"Anaya Knox",
"Ethan Benson      ",
"Sammy Pollard     ",
"Gerardo Todd      ",
"Khloe Brewer      ",
"Lorelei Padilla   ",
"Nathaly Fitzpatrick       ",
"August Manning    ",
"Cory Melton       ",
"Tobias Allison    ",
"Yaritza Gross     ",
"Walter Glenn      ",
"Nathanial Keller  ",
"Skyler Holmes     ",
"Marcelo Galvan    ",
"Reese Monroe      ",
"Jaeden Christian  ",
"Ahmad Rodriguez   ",
"Isabelle Guzman   ",
"Clara Shields     ",
"Nancy Wilkinson   ",
"Turner Maddox     ",
"Iliana Solis      ",
"Sanai Osborn      ",
"Alannah Woodward  ",
"Aryan Vasquez     ",
"Justice Vega      ",
"Rosemary Mckenzie ",
"Troy Fleming      ",
"Marisa Lamb       ",
"Adelyn Pitts      ",
"Rudy Conner       ",
"Trace Spencer     ",
"Javon Cuevas      ",
"Malcolm Kemp      ",
"Emmy Kirby",
"Jameson Collier   ",
"Oswaldo Contreras ",
"Edward Moran      ",
"Santino Preston   ",
"Arnav Kelly       ",
"Carlie Aguirre    ",
"Charlie Lynch     ",
"Derick Knight     ",
"Aden Livingston   ",
"Janae Davis       ",
"Sandra Benjamin   ",
"Macy Estes",
"Devyn Schultz     ",
"Nicole Rivers     ",
"Khalil Cabrera    ",
"Harper Snow       ",
"Mason Ruiz",
"Isiah Buckley     ",
"Mila Yates",
"Jaida Hanna       ",
"Sidney Rollins    ",
"Ari Dennis",
"Josue Oconnell    ",
"Urijah Carrillo   ",
"Clare Joseph      ",
"Vaughn Decker     ",
"Emma Estrada      ",
"Tamara Ayers      ",
"Sawyer Mendez     ",
"Matias Beltran    ",
"Desmond Rodgers   ",
"Rigoberto Williamson      ",
"Dangelo Hurley    ",
"Chris Mann",
"Clark Barber      ",
"Dominique Miles   ",
"Alvin Flowers     ",
"Kinley Burton     ",
"Cailyn Chang      ",
"Jovani Nicholson  ",
"Anthony Sweeney   ",
"Sam Buchanan      ",
"Annie Nelson      ",
"Zayne Boyle       ",
"Yadira Newman     ",
"Skyler Hicks      ",
"Meredith Dalton   ",
"Francis Gomez     ",
"Leilani Byrd      ",
"Solomon Morrison  ",
"Kiley Singleton   ",
"Mareli Juarez     ",
"Destiney Crane    ",
"Jay Pruitt",
"Cayden Vance      ",
"Ellis Frazier     ",
"Julissa Gilbert   ",
"Elise Gill",
"Harper Keith      ",
"Ariel Francis     ",
"Aydan Heath       ",
"Jazmine Harrington",
"Grayson Young     ",
"Savion Herman     ",
"Kennedy Adkins    ",
"Jaslyn Bass       ",
"Elisha Farrell    ",
"Orlando Hogan     ",
"Roselyn Mccann    ",
"Sariah Blankenship",
"Beau Andrade      ",
"Darius Berger     ",
"Selena Davies     ",
"Lyric Ferrell     ",
"Jasiah Mack       ",
"Liana Navarro     ",
"Aydin Mcgrath     ",
"Jada Conway       ",
"Amiyah Bray       ",
"Tia Sexton",
"Monique Robinson  ",
"Carlos Marsh      ",
"Haley Rose",
"Dakota Copeland   ",
"Edwin Ramsey      ",
"Yareli Little     ",
"Ruth Roy  ",
"Riya Calhoun      ",
"Nathan Briggs     ",
"Lucy Harris       ",
"Jeffery Daniels   ",
"Deja Mata ",
"Nylah Suarez      ",
"Ryan Avila",
"Haylee Glass      ",
"Riley Beck",
"Colby Campos      ",
"Kieran Vazquez    ",
"Omari Trevino     ",
"Madelyn Costa     ",
"Van Finley",
"Randy Carpenter   ",
"Devin Acosta      ",
"Nyla Cunningham   ",
"Alden Moore       ",
"Sarahi Soto       ",
"Shyla Wilkins     ",
"Sofia Lindsey     ",
"Ada Stanley       ",
"Kristin Villarreal",
"Maurice Bowman    ",
"Casey Murphy      ",
"Abagail Sawyer    ",
"Jefferson Malone  ",
"Colin Santana     ",
"Hudson Orozco     ",
"Eden Nichols      ",
"Lilia Holland     ",
"Reese Shaffer     ",
"Marilyn Hardy     ",
"Harrison Nunez    ",
"Olivia Cummings   ",
"Aidyn Goodwin     ",
"Royce Pratt       ",
"Corbin Mcgee      ",
"Liliana Ali       ",
"Thaddeus Reyes    ",
"Jakob Richards    ",
"Sylvia Hayden     ",
"Adrian Newton     ",
"Amaris Sellers    ",
"Leslie Watts      ",
"Jamya Fox ",
"Arielle Mcfarland ",
"Kimberly Kirk     ",
"Alanna Velez      ",
"Emily Medina      ",
"Ashlyn Solomon    ",
"Tony Russell      ",
"Ronin Hampton     ",
"Kamryn Shelton    ",
"Connor Roach      ",
"Marie Massey      ",
"Jaydon Reilly     ",
"Ricardo Acevedo   ",
"Matthias Riddle   ",
"Peyton Doyle      ",
"Nayeli Berry      ",
"Hailie Hendricks  ",
"Jayden Meadows    ",
"Jaycee Michael    ",
"Summer Cannon     ",
"Armani Reid       ",
"Jazmyn Rhodes     ",
"Madyson Day       ",
"Gary Everett      ",
"Thalia Miller     ",
"Allisson Cherry   ",
"Elian Donaldson   ",
"Braxton Johnson   ",
"Bruce Andrews     ",
"Zechariah Garner  ",
"Kaleb Haynes      ",
"Isabella Oconnor  ",
"Trinity Morris    ",
"Jamar Larson      ",
"Carson Meza       ",
"Clayton Cervantes ",
"Todd Wiggins      ",
"Keaton Henry      ",
"Cannon Walls      ",
"Julio Mitchell    ",
"Chace Poole       ",
"Eliza Douglas     ",
"Campbell Camacho  ",
"Jorden Hutchinson ",
"Rhys Bradshaw     ",
"Kymani Bailey     ",
"Geovanni Rice     ",
"Alexis Good       ",
"Haven Galloway    ",
"Miguel Diaz       ",
"Armani Tucker     ",
"Ralph Barker      ",
"Aileen Archer     ",
"Cali Schroeder    ",
"Julianne Nolan    ",
"Ray Macdonald     ",
"Asher Simmons     ",
"Myles Holloway    ",
"Marlee Cox",
"Brendon Tyler     ",
"Jessie Harrell    ",
"Danica Best       ",
"Mathew Fisher     ",
"Abril Oneal       ",
"Gabriela Wagner   ",
"Javier Blanchard  ",
"Owen Page ",
"Noemi Gardner     ",
"Johanna Perkins   ",
"Kenyon Avery      ",
"Madden Daugherty  ",
"Alice Bradford    ",
"Leon Vaughn       ",
"Maci Hooper       ",
"Rachael Irwin     ",
"Alyson Lynn       ",
"Brisa Gillespie   ",
"Magdalena Weeks   ",
"Donovan Santiago  ",
"Daniella Maxwell  ",
"Colton Schmidt    ",
"Deshawn Lawrence  ",
"Myah Parsons      ",
"Dahlia Adams      ",
"Keira Mckinney    ",
"Calvin Mullen     ",
"Braiden Mora      ",
"Paola Mayer       ",
"Koen Burch",
"Brady Cooke       ",
"Evan Bean ",
"Emilia Molina     ",
"Makena Yoder      ",
"Kade Jimenez      ",
"Savannah Chung    ",
"Elliot Erickson   ",
"Natasha Ponce     ",
"Titus Atkins      ",
"Iyana Benitez     ",
"Lawson Compton    ",
"Silas Ellison     ",
"Amaya Church      ",
"Brennan Gilmore   ",
"Charity Fuentes   ",
"Darnell Kaufman   ",
"Brooke Wallace    ",
"Lucille Paul      ",
"Giada Winters     ",
"Deangelo Hebert   ",
"Ernest Hurst      ",
"Colten Fletcher   ",
"Celia Richard     ",
"Tamia Rosales     ",
"Nathanael Martin  ",
"Jase Summers      ",
"Sean Montes       ",
"Cynthia Schaefer  ",
"Kamren Roth       ",
"Brayden Harvey    ",
"Taylor Jacobs     ",
"Trevin Odonnell   ",
"Daniela Rivas     ",
"Fabian Whitehead  ",
"Yael Mayo ",
"Patricia Stokes   ",
"Ashlynn Key       ",
"Bryan Steele      ",
"Pedro Nash",
"Cassidy Frederick ",
"Anne Huang",
"Rory Stevens      ",
"Anton Baird       ",
"Hanna Murray      ",
"Sydney Hill       ",
"Coleman Kent      ",
"Miley Murillo     ",
"Tommy Cole",
"Arely Davila      ",
"Wesley Harrison   ",
"Sullivan Savage   ",
"Damien Mays       ",
"Mckayla Schmitt   ",
"Cora Jennings     ",
"Nathalie Escobar  ",
"Sara Campbell     ",
"Mackenzie Whitney ",
"Payton Conrad     ",
"Paris Washington  ",
"Santos Peterson   ",
"Fiona Lawson      ",
"Karley Alvarez    ",
"Rylee Strong      ",
"Haiden Jenkins    ",
"Shannon Ewing     ",
"Izabella Cantu    ",
"Avery Carson      ",
"Wade Howard       ",
"Jaxson Craig      ",
"Jerome Pierce     ",
"Heaven Jensen     ",
"Chloe Perry       ",
"Jaxon Bridges     ",
"Alma Castro       ",
"Yurem Green       ",
"Ean Proctor       ",
"Angela Duarte     ",
"Sierra Kelley     ",
"Karter Stark      ",
"Alexia Waller     ",
"Alfredo Short     ",
"Declan Leon       ",
"Eugene Rasmussen  ",
"Rebecca Cooper    ",
"Yandel Cowan      ",
"Jillian Huynh     ",
"Alex Harmon       ",
"Michaela Flores   ",
"Jamison Hudson    ",
"Landen Rubio      ",
"Micah Ho  ",
"Zaria Reese       ",
"Haleigh Herrera   ",
"Olive Park",
"Alondra Phillips  ",
"Yazmin Norris     ",
"Courtney King     ",
"Carlo Figueroa    ",
"Felicity Chaney   ",
"Terrell Mcmillan  ",
"Kallie Chen       ",
"Zachary Miranda   ",
"Alfred Long       ",
"Lauryn Neal       ",
"Emmalee Grimes    ",
"Izabelle Duke     ",
"Giovanny Salazar  ",
"Quinn Haney       ",
"Addisyn Hodges    ",
"Adrien Alexander  ",
"Anika Hunter      ",
"Makenzie Stuart   ",
"Maggie Peters     ",
"Terrence Pena     ",
"Bronson Rush      ",
"Anabella Mcdonald ",
"Cade Mccarthy     ",
"Janelle Scott     ",
"Dana Dixon",
"Laura Caldwell    ",
"Lilianna Parks    ",
"Heidi Hickman     ",
"Jeramiah Cortez   ",
"Kayley Ballard    ",
"Trent House       ",
"Raul Bond ",
"Bennett Marks     ",
"Leandro Hess      ",
"Howard Marquez    ",
"Cindy Lewis       ",
"Peter Wong",
"Lawrence Gates    ",
"Esteban Fuller    ",
"Kiersten Hamilton ",
"Stacy Bryan       ",
"Xzavier Ashley    ",
"Belen Wu  ",
"Brenton Bruce     ",
"Ashanti Hendrix   ",
"Amber Martinez    ",
"Frida Stout       ",
"Cloe Roman",
"Andrew Flynn      ",
"Anaya Knox",
"Ethan Benson      ",
"Sammy Pollard     ",
"Gerardo Todd      ",
"Khloe Brewer      ",
"Lorelei Padilla   ",
"Nathaly Fitzpatrick       ",
"August Manning    ",
"Cory Melton       ",
"Tobias Allison    ",
"Yaritza Gross     ",
"Walter Glenn      ",
"Nathanial Keller  ",
"Skyler Holmes     ",
"Marcelo Galvan    ",
"Reese Monroe      ",
"Jaeden Christian  ",
"Ahmad Rodriguez   ",
"Isabelle Guzman   ",
"Clara Shields     ",
"Nancy Wilkinson   ",
"Turner Maddox     ",
"Iliana Solis      ",
"Sanai Osborn      ",
"Alannah Woodward  ",
"Aryan Vasquez     ",
"Justice Vega      ",
"Rosemary Mckenzie ",
"Troy Fleming      ",
"Marisa Lamb       ",
"Adelyn Pitts      ",
"Rudy Conner       ",
"Trace Spencer     ",
"Javon Cuevas      ",
"Malcolm Kemp      ",
"Emmy Kirby",
"Jameson Collier   ",
"Oswaldo Contreras ",
"Edward Moran      ",
"Santino Preston   ",
"Arnav Kelly       ",
"Carlie Aguirre    ",
"Charlie Lynch     ",
"Derick Knight     ",
"Aden Livingston   ",
"Janae Davis       ",
"Sandra Benjamin   ",
"Macy Estes",
"Devyn Schultz     ",
"Nicole Rivers     ",
"Khalil Cabrera    ",
"Harper Snow       ",
"Mason Ruiz",
"Isiah Buckley     ",
"Mila Yates",
"Jaida Hanna       ",
"Sidney Rollins    ",
"Ari Dennis",
"Josue Oconnell    ",
"Urijah Carrillo   ",
"Clare Joseph      ",
"Vaughn Decker     ",
"Emma Estrada      ",
"Tamara Ayers      ",
"Sawyer Mendez     ",
"Matias Beltran    ",
"Desmond Rodgers   ",
"Rigoberto Williamson      ",
"Urijah Carrillo   ",
"Clare Joseph      ",
"Vaughn Decker     ",
"Emma Estrada      ",
"Tamara Ayers      ",
"Sawyer Mendez     ",
"Matias Beltran    ",
"Desmond Rodgers   ",
"Rigoberto Williamson      ",
"Dangelo Hurley    ",
"Chris Mann",
"Clark Barber      ",
"Dominique Miles   ",
"Alvin Flowers     ",
"Kinley Burton     ",
"Cailyn Chang      ",
"Jovani Nicholson  ",
"Anthony Sweeney   ",
"Sam Buchanan      ",
"Annie Nelson      ",
"Zayne Boyle       ",
"Yadira Newman     ",
"Skyler Hicks      ",
"Meredith Dalton   ",
"Francis Gomez     ",
"Leilani Byrd      ",
"Solomon Morrison  ",
"Kiley Singleton   ",
"Mareli Juarez     ",
"Destiney Crane    ",
"Jay Pruitt",
"Cayden Vance      ",
"Ellis Frazier     ",
"Julissa Gilbert   ",
"Elise Gill",
"Harper Keith      ",
"Ariel Francis     ",
"Aydan Heath       ",
"Jazmine Harrington",
"Grayson Young     ",
"Savion Herman     ",
"Kennedy Adkins    ",
"Jaslyn Bass       ",
"Elisha Farrell    ",
"Orlando Hogan     ",
"Roselyn Mccann    ",
"Sariah Blankenship",
"Beau Andrade      ",
"Darius Berger     ",
"Selena Davies     ",
"Lyric Ferrell     ",
"Jasiah Mack       ",
"Liana Navarro     ",
"Aydin Mcgrath     ",
"Jada Conway       ",
"Amiyah Bray       ",
"Tia Sexton",
"Monique Robinson  ",
"Carlos Marsh      ",
"Haley Rose",
"Dakota Copeland   ",
"Edwin Ramsey      ",
"Yareli Little     ",
"Ruth Roy  ",
"Riya Calhoun      ",
"Nathan Briggs     ",
"Lucy Harris       ",
"Jeffery Daniels   ",
"Deja Mata ",
"Nylah Suarez      ",
"Ryan Avila",
"Haylee Glass      ",
"Riley Beck",
"Colby Campos      ",
"Kieran Vazquez    ",
"Omari Trevino     ",
"Madelyn Costa     ",
"Van Finley",
"Randy Carpenter   ",
"Devin Acosta      ",
"Nyla Cunningham   ",
"Alden Moore       ",
"Sarahi Soto       ",
"Shyla Wilkins     ",
"Sofia Lindsey     ",
"Ada Stanley       ",
"Kristin Villarreal",
"Maurice Bowman    ",
"Casey Murphy      ",
"Abagail Sawyer    ",
"Jefferson Malone  ",
"Colin Santana     ",
"Hudson Orozco     ",
"Eden Nichols      ",
"Lilia Holland     ",
"Reese Shaffer     ",
"Marilyn Hardy     ",
"Harrison Nunez    ",
"Olivia Cummings   ",
"Aidyn Goodwin     ",
"Royce Pratt       ",
"Corbin Mcgee      ",
"Liliana Ali       ",
"Thaddeus Reyes    ",
"Jakob Richards    ",
"Sylvia Hayden     ",
"Adrian Newton     ",
"Amaris Sellers    ",
"Leslie Watts      ",
"Jamya Fox ",
"Arielle Mcfarland ",
"Kimberly Kirk     ",
"Alanna Velez      ",
"Emily Medina      ",
"Ashlyn Solomon    ",
"Tony Russell      ",
"Ronin Hampton     ",
"Kamryn Shelton    ",
"Connor Roach      ",
"Marie Massey      ",
"Jaydon Reilly     ",
"Ricardo Acevedo   ",
"Matthias Riddle   ",
"Peyton Doyle      ",
"Nayeli Berry      ",
"Hailie Hendricks  ",
"Jayden Meadows    ",
"Jaycee Michael    ",
"Summer Cannon     ",
"Armani Reid       ",
"Jazmyn Rhodes     ",
"Madyson Day       ",
"Gary Everett      ",
"Thalia Miller     ",
"Allisson Cherry   ",
"Elian Donaldson   ",
"Braxton Johnson   ",
"Bruce Andrews     ",
"Zechariah Garner  ",
"Kaleb Haynes      ",
"Isabella Oconnor  ",
"Trinity Morris    ",
"Jamar Larson      ",
"Carson Meza       ",
"Clayton Cervantes ",
"Todd Wiggins      ",
"Keaton Henry      ",
"Cannon Walls      ",
"Julio Mitchell    ",
"Chace Poole       ",
"Eliza Douglas     ",
"Campbell Camacho  ",
"Jorden Hutchinson ",
"Rhys Bradshaw     ",
"Kymani Bailey     ",
"Geovanni Rice     ",
"Alexis Good       ",
"Haven Galloway    ",
"Miguel Diaz       ",
"Armani Tucker     ",
"Ralph Barker      ",
"Aileen Archer     ",
"Cali Schroeder    ",
"Julianne Nolan    ",
"Ray Macdonald     ",
"Asher Simmons     ",
"Myles Holloway    ",
"Marlee Cox",
"Brendon Tyler     ",
"Jessie Harrell    ",
"Danica Best       ",
"Mathew Fisher     ",
"Abril Oneal       ",
"Gabriela Wagner   ",
"Javier Blanchard  ",
"Owen Page ",
"Noemi Gardner     ",
"Johanna Perkins   ",
"Kenyon Avery      ",
"Madden Daugherty  ",
"Alice Bradford    ",
"Leon Vaughn       ",
"Maci Hooper       ",
"Rachael Irwin     ",
"Alyson Lynn       ",
"Brisa Gillespie   ",
"Magdalena Weeks   ",
"Donovan Santiago  ",
"Daniella Maxwell  ",
"Colton Schmidt    ",
"Deshawn Lawrence  ",
"Myah Parsons      ",
"Dahlia Adams      ",
"Keira Mckinney    ",
"Calvin Mullen     ",
"Braiden Mora      "
]

status_list =[
    "online",
    "busy",
    "dnd"
]
#print(names_list)
#SP:39:Test Char Speed:967180551::1::::E:01::0:0::1937:0:1:#000000:
user_id = 1000

for one_name in names_list:
    name, surname = one_name.strip().split(" ")
    print("{}.{};{};{};dn={} \"O\": \"Bank A\", \"role\": \"User\", \"CN\": \"{}.{}\" {};{};".format(name, surname, user_id, status_list[random.randint(0,2)], "{", name, surname, "}", one_name.strip()))
    user_id += 1
    #print("SP:{}:{}:967180551::1::::E:01::0:0::1937:0:1:#000000:".format(start_from, one_name.strip()))


