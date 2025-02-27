import unittest

from src.domain.plugin import PluginMetadata


class TestPluginMetadata(unittest.TestCase):

    def setUp(self):
        self.plugin_metadata = PluginMetadata(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author_name="Walter White",
            author_email="XXXXXXXXXXXXXXXX"
        )

    def test_should_generate_plugin_id_on_initialization(self):
        plugin_id = self.plugin_metadata.plugin_id
        self.assertTrue(plugin_id)

    def test_should_generate_last_updated_on_initialization(self):
        last_updated = self.plugin_metadata.last_updated
        self.assertTrue(last_updated)

    def test_should_update_metadata(self):
        self.plugin_metadata.update(
            name="Updated Plugin",
            description="This is an updated description.",
            version="2.0.0",
            author_name="Jesse Pinkman",
            author_email="XXXXXXXXXXXXXXXX"
        )

        self.assertEqual(self.plugin_metadata.name, "Updated Plugin")
        self.assertEqual(self.plugin_metadata.description, "This is an updated description.")
        self.assertEqual(self.plugin_metadata.version, "2.0.0")
        self.assertEqual(self.plugin_metadata.author_name, "Jesse Pinkman")
        self.assertEqual(self.plugin_metadata.author_email, "XXXXXXXXXXXXXXXX")

    def test_should_update_last_updated(self):
        before = self.plugin_metadata.last_updated
        self.plugin_metadata.update(
            name="Updated Plugin",
            description="This is an updated description.",
            version="2.0.0",
            author_name="Jesse Pinkman",
            author_email="XXXXXXXXXXXXXXXX"
        )

        after = self.plugin_metadata.last_updated
        self.assertTrue(before < after)

    def test_should_return_false_for_same_version(self):
        current_version = self.plugin_metadata.version
        version_has_changed = self.plugin_metadata.version_has_changed(current_version)
        self.assertFalse(version_has_changed)

    def test_should_return_true_for_downgrade(self):
        new_version = '1.9'
        version_has_changed = self.plugin_metadata.version_has_changed(new_version)
        self.assertTrue(version_has_changed)

    def test_should_return_true_for_upgrade(self):
        current_version = '2.0.1'
        version_has_changed = self.plugin_metadata.version_has_changed(current_version)
        self.assertTrue(version_has_changed)
