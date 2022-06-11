def paginate(total_pages, current_page, boundaries, around):

    pages = list()
    all_pages = list(range(1, total_pages + 1))

    for page in all_pages:
        if page <= boundaries or page > total_pages - boundaries or page == current_page:
            pages.append(page)

    return pages

if __name__ == '__main__':
    paginate(5, 4, 1, 0)
