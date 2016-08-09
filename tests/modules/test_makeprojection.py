import StringIO
import base64
import unittest
import zlib

import cellprofiler.image
import cellprofiler.measurement
import cellprofiler.module
import cellprofiler.modules.makeprojection
import cellprofiler.pipeline
import cellprofiler.preferences
import cellprofiler.region
import cellprofiler.workspace
import numpy

cellprofiler.preferences.set_headless()

IMAGE_NAME = 'image'
PROJECTED_IMAGE_NAME = 'projectedimage'


class TestMakeProjection(unittest.TestCase):
    def test_01_02_load_v1(self):
        data = ('eJztWd1OGkEUHn60WtuGXrVJb+ZSWtgsaBskjYLStLSiRImNMbYdYYBpd3fI'
                'MGuljUkfq5d9lD5CH6EzuAvsCiwgupqwyQTP2fPNN+c7O7szYyFb2s5uwpeK'
                'CgvZUrxKNAyLGuJVyvQ0NHgMbjGMOK5AaqRhqW7C96YGE6+gmkqvpNKrKkyq'
                '6hqY7ArkC4/Ej/oMgHnxuyBa0Lo1Z9mBnibtfcw5MWrNORAGTy3/H9EOECPo'
                'RMMHSDNxs0th+/NGlZZajc6tAq2YGt5Bem+wuHZM/QSz5m7VBlq3i+QMa/vk'
                'B3alYIft4VPSJNSw8Fb/bm+Hl3IXr9Th71JXh4BLh5BokR6/jH8HuvHhPro9'
                '7omPWDYxKuSUVEykQaKjWmcUsr+UR39zrv6kvUU1ykbE33Phpb3LSG0PV9r4'
                'jAc+4sLLVsJnPP7mDJU51BEv1yfNY7+hEX6FPLKnmAk523jVAx9w4ANgZUTe'
                'BeDkXbD0e8tQaxT9Hrrw0i4y+hWXuXhGZRXASHW47+pH2jkKDcqh2bQmyCg6'
                'hBz9hEBCUS/h5l04+7Jxi2B0vqCDLwh2qD/j9Jq3T4BTX2nncBWZGod5OWlh'
                'jjBRNMpavus8zfq4x3ko3k5+8F31PeanPpM+9zcxzzIeuEXg1FXaF+83jI0B'
                '/NepLydVX/S97u/woO/Iplg6Xae+7u9eog/uNryHwo5xhkU9janpMg7ul8c4'
                'PwBnHaX9aXmj+Fou4PG68iL6WVofsabt0e/rR9l48Thqe8QDY+rG+pEaXzv+'
                'mYglzy+C94lAtp3RK49/UlzdI++UK29py7EfYsSshFbPo3HpKlCD1y1f0vLl'
                'UKvr8SO/5THX+ZPyZDx07LeOa28Kaoyajen34+c8vwlcBgzXqd/+pasTFFsz'
                '3JhmP3dFtxluhvNjnt2VfGf63k5cBkxHp2n1c1d0m+FmuLH2A4HB62X3vl3G'
                'fwHD59Nz4JxP0i6LLVGDUfn/D6bo7UP6pqJRVLk4JVe2xZ/5ngPzUXhiLp7Y'
                'IJ6y3LxzWmOopbQ38iUqz3Q7+XvwJF08yUE8OvqGG50DX6UgzO75b/86Lfbh'
                '69U7KKzIg9DQ+gLgrGu33v82JuELBQKXzjmWPHDhnjHZef4G4z1Xy0Pi7Rxv'
                'Kv4/DzlPxw==')
        pipeline = cellprofiler.pipeline.Pipeline()

        def callback(caller, event):
            self.assertFalse(isinstance(event, cellprofiler.pipeline.LoadExceptionEvent))

        pipeline.add_listener(callback)
        pipeline.load(StringIO.StringIO(zlib.decompress(base64.b64decode(data))))
        module = pipeline.modules()[2]
        self.assertTrue(isinstance(module, cellprofiler.modules.makeprojection.MakeProjection))
        self.assertEqual(module.image_name.value, "OrigRed")
        self.assertEqual(module.projection_image_name.value, "ProjectionRed")
        self.assertEqual(module.projection_type, cellprofiler.modules.makeprojection.P_AVERAGE)

    def test_01_03_load_v2(self):
        data = r"""CellProfiler Pipeline: http://www.cellprofiler.org
Version:1
SVNRevision:10000

MakeProjection:[module_num:1|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Average
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:2|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Maximum
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:3|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Minimum
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:4|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Sum
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:5|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Variance
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:6|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Power
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6

MakeProjection:[module_num:7|svn_version:\'9999\'|variable_revision_number:2|show_window:False|notes:\x5B\x5D]
    Select the input image:ch02
    Type of projection:Brightfield
    Name the output image:ProjectionCh00Scale6
    Frequency\x3A:6
"""
        pipeline = cellprofiler.pipeline.Pipeline()

        def callback(caller, event):
            self.assertFalse(isinstance(event, cellprofiler.pipeline.LoadExceptionEvent))

        pipeline.load(StringIO.StringIO(data))
        methods = (cellprofiler.modules.makeprojection.P_AVERAGE, cellprofiler.modules.makeprojection.P_MAXIMUM, cellprofiler.modules.makeprojection.P_MINIMUM, cellprofiler.modules.makeprojection.P_SUM, cellprofiler.modules.makeprojection.P_VARIANCE,
                   cellprofiler.modules.makeprojection.P_POWER, cellprofiler.modules.makeprojection.P_BRIGHTFIELD)
        self.assertEqual(len(pipeline.modules()), len(methods))
        for method, module in zip(methods, pipeline.modules()):
            self.assertTrue(isinstance(module, cellprofiler.modules.makeprojection.MakeProjection))
            self.assertEqual(module.image_name, "ch02")
            self.assertEqual(module.projection_type, method)
            self.assertEqual(module.projection_image_name, "ProjectionCh00Scale6")
            self.assertEqual(module.frequency, 6)

    def run_image_set(self, projection_type, images_and_masks,
                      frequency=9, run_last=True):
        image_set_list = cellprofiler.image.ImageSetList()
        image_count = len(images_and_masks)
        for i in range(image_count):
            pixel_data, mask = images_and_masks[i]
            if mask is None:
                image = cellprofiler.image.Image(pixel_data)
            else:
                image = cellprofiler.image.Image(pixel_data, mask)
            image_set_list.get_image_set(i).add(IMAGE_NAME, image)
        #
        # Add bogus image at end for 2nd group
        #
        bogus_image = cellprofiler.image.Image(numpy.zeros((10, 20)))
        image_set_list.get_image_set(image_count).add(IMAGE_NAME, bogus_image)

        pipeline = cellprofiler.pipeline.Pipeline()
        module = cellprofiler.modules.makeprojection.MakeProjection()
        module.module_num = 1
        module.image_name.value = IMAGE_NAME
        module.projection_image_name.value = PROJECTED_IMAGE_NAME
        module.projection_type.value = projection_type
        module.frequency.value = frequency
        pipeline.add_module(module)
        m = cellprofiler.measurement.Measurements()
        workspace = cellprofiler.workspace.Workspace(pipeline, module, None, None, m, image_set_list)
        module.prepare_run(workspace)
        module.prepare_group(workspace, {}, range(1, len(images_and_masks) + 1))
        for i in range(image_count):
            w = cellprofiler.workspace.Workspace(pipeline, module,
                                                 image_set_list.get_image_set(i),
                                                 cellprofiler.region.Set(),
                                                 m,
                                                 image_set_list)
            if i < image_count - 1 or run_last:
                module.run(w)
        module.post_group(w, {})
        image = w.image_set.get_image(PROJECTED_IMAGE_NAME)
        #
        # Make sure that the image provider is reset after prepare_group
        #
        module.prepare_group(workspace, {}, [image_count + 1])
        image_set = image_set_list.get_image_set(image_count)
        w = cellprofiler.workspace.Workspace(pipeline, module,
                                             image_set,
                                             cellprofiler.region.Set(),
                                             m,
                                             image_set_list)
        module.run(w)
        image_provider = image_set.get_image_provider(PROJECTED_IMAGE_NAME)
        self.assertEqual(numpy.max(image_provider.count), 1)

        return image

    def test_02_01_average(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)).astype(numpy.float32), None)
                            for i in range(3)]
        expected = numpy.zeros((10, 10), numpy.float32)
        for image, mask in images_and_masks:
            expected += image
        expected = expected / len(images_and_masks)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_AVERAGE, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) <
                                  numpy.finfo(float).eps))

    def test_02_02_average_mask(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(100, 100)).astype(numpy.float32),
                             numpy.random.uniform(size=(100, 100)) > .3)
                            for i in range(3)]
        expected = numpy.zeros((100, 100), numpy.float32)
        expected_count = numpy.zeros((100, 100), numpy.float32)
        expected_mask = numpy.zeros((100, 100), bool)
        for image, mask in images_and_masks:
            expected[mask] += image[mask]
            expected_count[mask] += 1
            expected_mask = mask | expected_mask
        expected = expected / expected_count
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_AVERAGE, images_and_masks)
        self.assertTrue(image.has_mask)
        self.assertTrue(numpy.all(expected_mask == image.mask))
        numpy.testing.assert_almost_equal(image.pixel_data[image.mask],
                                          expected[expected_mask])

    def test_02_03_average_color(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10, 3)).astype(numpy.float32), None) for i in range(3)]
        expected = numpy.zeros((10, 10, 3), numpy.float32)

        for image, mask in images_and_masks:
            expected += image

        expected /= len(images_and_masks)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_AVERAGE, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) < numpy.finfo(float).eps))

    def test_02_04_average_masked_color(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10, 3)).astype(numpy.float32),
                             numpy.random.uniform(size=(10, 10)) > .3)
                            for i in range(3)]
        expected = numpy.zeros((10, 10, 3))
        expected_count = numpy.zeros((10, 10), numpy.float32)
        expected_mask = numpy.zeros((10, 10), bool)
        for image, mask in images_and_masks:
            expected[mask, :] += image[mask, :]
            expected_count[mask] += 1
            expected_mask = mask | expected_mask
        expected = expected / expected_count[:, :, numpy.newaxis]
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_AVERAGE, images_and_masks)
        self.assertTrue(image.has_mask)
        numpy.testing.assert_equal(image.mask, expected_mask)
        numpy.testing.assert_almost_equal(image.pixel_data[expected_mask],
                                          expected[expected_mask])

    def test_03_01_maximum(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)).astype(numpy.float32), None)
                            for i in range(3)]
        expected = numpy.zeros((10, 10), numpy.float32)
        for image, mask in images_and_masks:
            expected = numpy.maximum(expected, image)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MAXIMUM, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) <
                                  numpy.finfo(float).eps))

    def test_03_02_maximum_mask(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(100, 100)).astype(numpy.float32),
                             numpy.random.uniform(size=(100, 100)) > .3)
                            for i in range(3)]
        expected = numpy.zeros((100, 100), numpy.float32)
        expected_mask = numpy.zeros((100, 100), bool)
        for image, mask in images_and_masks:
            expected[mask] = numpy.maximum(expected[mask], image[mask])
            expected_mask = mask | expected_mask
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MAXIMUM, images_and_masks)
        self.assertTrue(image.has_mask)
        self.assertTrue(numpy.all(expected_mask == image.mask))
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data[image.mask] -
                                            expected[expected_mask]) <
                                  numpy.finfo(float).eps))

    def test_03_03_maximum_color(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10, 3)).astype(numpy.float32), None)
                            for i in range(3)]
        expected = numpy.zeros((10, 10, 3), numpy.float32)
        for image, mask in images_and_masks:
            expected = numpy.maximum(expected, image)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MAXIMUM, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) <
                                  numpy.finfo(float).eps))

    def test_04_01_variance(self):
        numpy.random.seed(41)
        images_and_masks = [(numpy.random.uniform(size=(20, 10)).astype(numpy.float32), None)
                            for i in range(10)]
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_VARIANCE, images_and_masks)
        images = numpy.array([x[0] for x in images_and_masks])
        x = numpy.sum(images, 0)
        x2 = numpy.sum(images ** 2, 0)
        expected = x2 / 10.0 - x ** 2 / 100.0
        numpy.testing.assert_almost_equal(image.pixel_data, expected, 4)

    def test_05_01_power(self):
        image = numpy.ones((20, 10))
        images_and_masks = [(image.copy(), None) for i in range(9)]
        for i, (img, _) in enumerate(images_and_masks):
            img[5, 5] *= numpy.sin(2 * numpy.pi * float(i) / 9.0)
        image_out = self.run_image_set(cellprofiler.modules.makeprojection.P_POWER, images_and_masks, frequency=9)
        i, j = numpy.mgrid[:image.shape[0], :image.shape[1]]
        numpy.testing.assert_almost_equal(image_out.pixel_data[(i != 5) & (j != 5)], 0)
        self.assertTrue(image_out.pixel_data[5, 5] > 1)

    def test_06_01_brightfield(self):
        image = numpy.ones((20, 10))
        images_and_masks = [(image.copy(), None) for i in range(9)]
        for i, (img, _) in enumerate(images_and_masks):
            if i < 5:
                img[:5, :5] = 0
            else:
                img[:5, 5:] = 0
        image_out = self.run_image_set(cellprofiler.modules.makeprojection.P_BRIGHTFIELD, images_and_masks)
        i, j = numpy.mgrid[:image.shape[0], :image.shape[1]]
        numpy.testing.assert_almost_equal(image_out.pixel_data[(i > 5) | (j < 5)], 0)
        numpy.testing.assert_almost_equal(image_out.pixel_data[(i < 5) & (j >= 5)], 1)

    def test_07_01_minimum(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)).astype(numpy.float32), None)
                            for i in range(3)]
        expected = numpy.ones((10, 10), numpy.float32)
        for image, mask in images_and_masks:
            expected = numpy.minimum(expected, image)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MINIMUM, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) <
                                  numpy.finfo(float).eps))

    def test_07_02_minimum_mask(self):
        numpy.random.seed(72)
        images_and_masks = [(numpy.random.uniform(size=(100, 100)).astype(numpy.float32),
                             numpy.random.uniform(size=(100, 100)) > .3)
                            for i in range(3)]
        expected = numpy.ones((100, 100), numpy.float32)
        expected_mask = numpy.zeros((100, 100), bool)
        for image, mask in images_and_masks:
            expected[mask] = numpy.minimum(expected[mask], image[mask])
            expected_mask = mask | expected_mask
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MINIMUM, images_and_masks)
        self.assertTrue(image.has_mask)
        self.assertTrue(numpy.any(image.mask == False))
        self.assertTrue(numpy.all(expected_mask == image.mask))
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data[image.mask] -
                                            expected[expected_mask]) <
                                  numpy.finfo(float).eps))
        self.assertTrue(numpy.all(image.pixel_data[~image.mask] == 0))

    def test_07_03_minimum_color(self):
        numpy.random.seed(0)
        images_and_masks = [(numpy.random.uniform(size=(10, 10, 3)).astype(numpy.float32), None)
                            for i in range(3)]
        expected = numpy.ones((10, 10, 3), numpy.float32)
        for image, mask in images_and_masks:
            expected = numpy.minimum(expected, image)
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MINIMUM, images_and_masks)
        self.assertFalse(image.has_mask)
        self.assertTrue(numpy.all(numpy.abs(image.pixel_data - expected) <
                                  numpy.finfo(float).eps))

    def test_08_01_mask_unmasked(self):
        numpy.random.seed(81)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)), None)
                            for i in range(3)]
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MASK, images_and_masks)
        self.assertEqual(tuple(image.pixel_data.shape), (10, 10))
        self.assertTrue(numpy.all(image.pixel_data == True))
        self.assertFalse(image.has_mask)

    def test_08_02_mask(self):
        numpy.random.seed(81)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)),
                             numpy.random.uniform(size=(10, 10)) > .3)
                            for i in range(3)]
        expected = numpy.ones((10, 10), bool)
        for _, mask in images_and_masks:
            expected = expected & mask
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_MASK, images_and_masks)
        self.assertTrue(numpy.all(image.pixel_data == expected))

    def test_09_02_filtered(self):
        '''Make sure the image shows up in the image set even if filtered

        This is similar to issue # 310 - the last image may be filtered before
        the projection is done and the aggregate image is then missing
        from the image set.
        '''
        numpy.random.seed(81)
        images_and_masks = [(numpy.random.uniform(size=(10, 10)), None)
                            for i in range(3)]
        image = self.run_image_set(cellprofiler.modules.makeprojection.P_AVERAGE, images_and_masks,
                                   run_last=False)
        numpy.testing.assert_array_almost_equal(
                image.pixel_data,
                (images_and_masks[0][0] + images_and_masks[1][0]) / 2)