const search = document.getElementById('course-search');
const year = document.getElementById('course-year');
const courses = Array.from(document.querySelectorAll('.course'));
const count = document.getElementById('course-count');
const empty = document.getElementById('course-empty');
function filterCourses() {
  const query = search.value.trim().toLocaleLowerCase();
  let visible = 0;
  for (const course of courses) {
    const matches = (year.value === 'all' || course.dataset.year === year.value) && course.dataset.search.toLocaleLowerCase().includes(query);
    course.hidden = !matches;
    if (matches) visible++;
  }
  count.textContent = `${visible} of ${courses.length} course and requirement references`;
  empty.hidden = visible !== 0;
}
search.addEventListener('input', filterCourses);
year.addEventListener('change', filterCourses);
filterCourses();
