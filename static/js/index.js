// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = (app) => {

  // This is the Vue data.
  app.data = {
    title: "",
    body: "",
    photos: "",
    radius: 0,
    stories: []
  };

  app.methods = {
    submitStory() {
      fetch(submit_story_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: this.title,
          body: this.body,
          photos: this.photos.split(','),
          radius: this.radius
        })
      })
        .then(response => response.json())
        .then(data => {
          console.log("Story Submitted");
          console.log("Story ID:", data.story_id);
          this.getStories(); // Refresh the story list
          // You can add any additional logic here, such as displaying a success message or redirecting to a different page.
        })
        .catch(error => {
          console.error("Error submitting story:", error);
        });
    },
    getStories() {
      fetch(get_stories_url, {
        method: 'GET'
      })
        .then(response => response.json())
        .then(data => {
          this.stories = data.stories;
        })
        .catch(error => {
          console.error("Error getting stories:", error);
        });
    },
    vote(storyId, value) {
      fetch(vote_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          story_id: storyId,
          value: value
        })
      })
        .then(response => response.json())
        .then(data => {
          console.log("Vote submitted successfully");
          this.getStories(); // Refresh the story list
        })
        .catch(error => {
          console.error("Error submitting vote:", error);
        });
    }
  };

  // This creates the Vue instance.
  app.vue = new Vue({
    el: "#vue-target",
    data: app.data,
    methods: app.methods,
    created() {
      this.getStories();
    }
  });

  // And this initializes it.
  app.init = () => {
    // Put here any initialization code.
  };

  // Call to the initializer.
  app.init();
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it.
init(app);
