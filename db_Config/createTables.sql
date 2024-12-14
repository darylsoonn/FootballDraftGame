CREATE TABLE Players (
    PlayerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Number INT,
    Pace INT,
    Shooting INT,
    Passing INT,
    Dribbling INT,
    Defending INT,
    Physical INT,
    Accolades TEXT,
    Age INT,
    Country VARCHAR(50),
    Club VARCHAR(100),
    MarketValue INT,
    Height FLOAT,
    Weight FLOAT
);

CREATE TABLE Drafts (
    DraftID INT PRIMARY KEY AUTO_INCREMENT,
    PlayerID INT,
    DraftedBy VARCHAR(100),
    Round INT,
    PickOrder INT,
    DraftStatus BOOLEAN,
    DraftedDate DATETIME,
    Notes TEXT,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);
