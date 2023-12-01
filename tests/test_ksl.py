def test_login_to_ksl(ksl, py):
    ksl.login()

    assert py.should().contain_title('My KSL')

def test_click_on_add_listing_button(login_to_ksl, ksl, py):
    ksl.create_new_listing()

    assert py.should().contain_title('Post FREE classifieds')

def test_upload_photos_to_listing(login_to_ksl, ksl, items, py):
    total_photos = sum(len(item.photoPaths) for item in items)

    ksl.create_new_listing()
    for item in items:
        ksl.upload_photos(item)

    photo_containers = py.find("div [class='photo-container']")
    assert len(photo_containers) == total_photos, "Number of photo containers does not match expected number"

