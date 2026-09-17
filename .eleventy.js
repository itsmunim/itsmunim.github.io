// Eleventy config — static site for itsmunim.github.io
// Markdown in /content becomes pre-rendered pages under /blog/<name>/.
module.exports = function (eleventyConfig) {
  // Explicit passthrough copies (passthroughFileCopy is disabled below)
  eleventyConfig.addPassthroughCopy("styles.css");
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("favicon");
  eleventyConfig.addPassthroughCopy("site.webmanifest");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("llms.txt");

  // "2026-09-17" -> "Sep 17, 2026"
  eleventyConfig.addFilter("readableDate", function (dateObj) {
    if (!dateObj) return "";
    const d = new Date(dateObj);
    return d.toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  });

  // "2026-09-17" -> "2026-09-17" (ISO, for <time datetime>)
  eleventyConfig.addFilter("dateISO", function (dateObj) {
    if (!dateObj) return "";
    return new Date(dateObj).toISOString().slice(0, 10);
  });

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
    },
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    passthroughFileCopy: false,
  };
};