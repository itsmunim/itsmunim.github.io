// Applies to every markdown file directly inside /content.
// One file = one blog post, rendered at /blog/<filename>/.
module.exports = {
  layout: "post.njk",
  tags: ["post"],
  permalink: (data) => `/blog/${data.page.fileSlug}/index.html`,
};