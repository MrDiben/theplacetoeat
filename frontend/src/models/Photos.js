//             "id": 20,
//             "filename": "3584-37.jpg",
//             "width": 3620,
//             "height": 2410,
//             "url": "https://lh3.googleusercontent.com/p/AF1QipO1TXrewGBv9yvyk37vhS57X4EASk0NYy5FOrdT=s1600-w500-h500",
//             "google_photo_reference": "CmRaAAAA_ZwLykS18lNdiMPOMV1AhCo9V1WA4sZedqGBgdJGiXP3K2l922cHdUQKQUn9YKVgMEsAxc9XMqiYzeAUZStPHZO1DHZKSM35uJoL0IzQa4ZerEmvRdyycoaWqFEBTUfBEhDpQWgrBNYjJKyr8oMAbGU8GhSVEuA5AsuEOde0abgke38N_mZufw",
//             "restaurant": 10
//         },

export default class Photo {
  constructor(photo) {
    this.setData(photo);
  }

  setData(photo) {
    if (!photo) {
      photo = {};
    }
    this.filename = photo.filename ? photo.filename : "";
    this.width = photo.width ? photo.width : null;
    this.height = photo.height ? photo.height : null;
    this.url = photo.url ? photo.url : "";
    this.google_photo_reference = photo.google_photo_reference
      ? photo.google_photo_reference
      : "";
  }
}
