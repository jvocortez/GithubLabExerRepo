db = connect("localhost:27017/musicDatabase");

db.artists.insertOne({
  ArtistId: 1,
  Name: "Sample Artist",
  Albums: [1]
});

db.albums.insertOne({
  AlbumId: 1,
  Title: "Sample Album",
  ArtistId: 1,
  Tracks: [1]
});

db.tracks.insertOne({
  TrackId: 1,
  Name: "Sample Track",
  AlbumId: 1,
  MediaTypeId: 1,
  GenreId: 1,
  Composer: "Sample Composer",
  Milliseconds: 250000,
  Bytes: 1024000,
  UnitPrice: 0.99
});
