"""fa"""

from atlanta_shore.data import abstract_image_processor


class SkyImage(abstract_image_processor.AbstractImageProcessor):
    def process_image(self):
        sky_amount = self.calculate_sky_amount()
        metadata = self.exif_data.get_metadata()
        metadata["sky_amount"] = sky_amount
        self.save_metadata_to_db(metadata)

    def calculate_sky_amount(self):
        # Implement sky amount calculation logic
        sky_amount = 0.75  # Placeholder value
        return sky_amount
