-- List the season number & title of the 1st episode of every season --
SELECT "season", "title" FROM "episodes" WHERE "episode_in_season" = 1;
